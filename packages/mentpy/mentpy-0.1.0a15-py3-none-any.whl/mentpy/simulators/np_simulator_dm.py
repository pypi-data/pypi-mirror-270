# Copyright 2023 Luis Mantilla
#
# Licensed under the Apache License, Version 2.0.
# See <http://www.apache.org/licenses/LICENSE-2.0> for details.
"""A density matrix simulator that uses numpy to simulate the quantum circuit."""

from typing import Union, List, Tuple, Optional

import numpy as np
import math
import networkx as nx

from mentpy.operators import Ment, ControlledMent
from mentpy.mbqc.mbqcircuit import MBQCircuit
from mentpy.simulators.base_simulator import BaseSimulator

from mentpy.operators import gates

import mentpy.calculator as calc

__all__ = ["NumpySimulatorDM"]


# COMMON QUANTUM STATES
q_zero = np.array([1, 0])
qubit_plus = gates.HGate @ q_zero


class NumpySimulatorDM(BaseSimulator):
    """A density matrix simulator that uses numpy to simulate the quantum circuit.

    Group
    -----
    simulators
    """

    # TODO: CALCULATE OPTIMAL WINDOW SIZE AUTOMATICALLY
    def __init__(
        self, mbqcircuit: MBQCircuit, input_state: np.ndarray = None, **kwargs
    ) -> None:
        super().__init__(mbqcircuit, input_state)

        self.window_size = kwargs.pop("window_size", 1)
        self.schedule = kwargs.pop("schedule", None)
        self.force0 = kwargs.pop("force0", True)
        self.dev_mode = kwargs.pop("dev_mode", False)
        self.wires = kwargs.pop("wires", None)

        if not self.force0:
            raise NotImplementedError("Numpy simulator does not support force0=False.")

        # TODO: FIND SCHEDULE IF NOT PROVIDED
        if self.schedule is not None:
            self.schedule_measure = [
                i for i in self.schedule if i not in mbqcircuit.quantum_output_nodes
            ]
        elif mbqcircuit.measurement_order is not None:
            # remove output nodes from the measurement order
            self.schedule_measure = [
                i
                for i in mbqcircuit.measurement_order
                if i not in mbqcircuit.quantum_output_nodes
            ]
            self.schedule = mbqcircuit.measurement_order
            if self.window_size == 1 and mbqcircuit.flow is not None:
                self.window_size = len(mbqcircuit.input_nodes) + 1
        else:
            raise ValueError(
                "Schedule must be provided for numpy simulator as the MBQCircuit does not have a flow."
            )

        input_state = self.reorder_qubits(
            input_state,
            self.mbqcircuit.input_nodes,
            self.schedule[: len(self.mbqcircuit.input_nodes)],
        )
        self.input_state = input_state

        n_qubits_input = len(mbqcircuit.input_nodes)

        if n_qubits_input > self.window_size:
            raise ValueError(
                f"Input state has {n_qubits_input} qubits, but window size is set to {self.window_size}."
                " Input state must have at most as many qubits as the window size minus one."
            )

        if self.window_size > len(self.schedule_measure):
            raise ValueError(
                f"Window size is set to {self.window_size}, but schedule only has {len(self.schedule_measure)} measurements."
            )

        self.current_measurement = 0

        for i in range(self.window_size - n_qubits_input):
            self.input_state = np.kron(self.input_state, qubit_plus)

        self.qstate = calc.pure2density(self.input_state)
        # get subgraph of the first window_size nodes
        self.subgraph = self.mbqcircuit.graph.subgraph(
            self.schedule[: self.window_size]
        )

        self.initial_czs = np.eye(2**self.window_size)

        if self.dev_mode:
            self._current_simulated_nodes = self.schedule[0 : self.window_size]

        # apply cz gates to neighboring qubits
        for node in self.subgraph.nodes:
            for neighbour in self.subgraph.neighbors(node):
                # avoid repeated application of cz gates
                if node < neighbour:
                    indx = self.current_simulated_nodes().index(node)
                    indy = self.current_simulated_nodes().index(neighbour)
                    cz = gates.controlled_z(indx, indy, self.window_size)
                    # self.qstate = cz @ self.qstate @ np.conj(cz).T
                    self.initial_czs = cz @ self.initial_czs

        self.qstate = self.initial_czs @ self.qstate @ np.conj(self.initial_czs).T
        self.outcomes = {}

    def current_simulated_nodes(self) -> List[int]:
        """Returns the nodes that are currently simulated."""
        if not self.dev_mode:
            return self.schedule[
                self.current_measurement : self.current_measurement + self.window_size
            ]
        elif self.dev_mode:
            return self._current_simulated_nodes

    def current_number_simulated_nodes(self) -> int:
        """Returns the number of nodes that are currently simulated."""
        n = self.window_size
        return min(n, len(self.mbqcircuit) - self.current_measurement)

    def node_in_which_wire(self, node: int) -> int:
        """Returns the wire in which the node is."""
        for i, wire in enumerate(self.wires):
            if node in wire:
                return i

    def neighbors_in_wire(self, node: int) -> List[int]:
        """Returns the neighbors of a node in the same wire."""
        wire = self.wires[self.node_in_which_wire(node)]
        # return nodes that have edges with node
        return [n for n in wire if self.mbqcircuit.graph.has_edge(node, n)]

    def future_neighbors_in_wire(self, node: int) -> List[int]:
        neighs = self.neighbors_in_wire(node)
        future_neighs = []
        for neigh in neighs:
            if neigh > node:
                future_neighs.append(neigh)
        return future_neighs

    def measure(self, angle: float, mode="sample") -> Tuple:
        if self.current_measurement >= len(self.schedule_measure):
            raise ValueError("No more measurements to be done.")

        if not self.dev_mode:
            current_ment = self.mbqcircuit[
                self.schedule_measure[self.current_measurement]
            ].copy()
            indx = 0
        elif self.dev_mode:
            # if in dev mode, we measure the first node in the current_simulated_nodes
            # only if a neighbor in the same wire is also in the current_simulated_nodes
            for node in self.current_simulated_nodes():
                cond = False
                futnods = self.future_neighbors_in_wire(node)
                if len(futnods) == 0:
                    cond = True
                else:
                    cond = futnods[0] in self.current_simulated_nodes()
                if cond:
                    current_ment = self.mbqcircuit[node].copy()
                    indx = self.current_simulated_nodes().index(node)
                    break

        self.qstate, outcome = self.measure_ment(
            current_ment, angle, indx, force0=self.force0, mode=mode
        )
        # check if qstate has nan
        if np.isnan(self.qstate).any():
            raise ValueError(
                "qstate has nan, you might want to increase the window size"
            )
        self.current_measurement += 1

        self.qstate = calc.partial_trace(self.qstate, [indx])

        if self.dev_mode:
            # remove qubit at indx from current_simulated_nodes
            self._current_simulated_nodes = [
                i for i in self._current_simulated_nodes if i != node
            ]
            if self.current_measurement + self.window_size <= len(
                self.mbqcircuit.graph.nodes
            ):
                self._current_simulated_nodes.append(
                    self.schedule[self.current_measurement + self.window_size - 1]
                )

        if self.current_measurement + self.window_size <= len(
            self.mbqcircuit.graph.nodes
        ):
            self.qstate = np.kron(self.qstate, calc.pure2density(qubit_plus))
            new_qubit = self.current_simulated_nodes()[-1]

            # get neighbours of new qubit
            neighbours = nx.neighbors(self.mbqcircuit.graph, new_qubit)

            # do cz between new qubit and neighbours
            indx_new = self.current_simulated_nodes().index(new_qubit)
            for neighbour in neighbours:
                if neighbour in self.current_simulated_nodes():
                    indxn = self.current_simulated_nodes().index(neighbour)
                    cz = gates.controlled_z(indxn, indx_new, self.window_size)
                    self.qstate = cz @ self.qstate @ np.conj(cz.T)

        return self.qstate, outcome

    def run(
        self, angles: List[float], mode="sample", input_state=None
    ) -> Tuple[List[int], np.ndarray]:
        """Measures the quantum state in the given pattern."""
        if input_state is not None:
            self.reset(input_state=input_state)

        if len(angles) != len(self.mbqcircuit.trainable_nodes):
            raise ValueError(
                f"Number of angles ({len(angles)}) does not match number of trainable nodes ({len(self.mbqcircuit.trainable_nodes)})."
            )

        if not self.dev_mode:
            for i in self.schedule_measure:
                if i in self.mbqcircuit.trainable_nodes:
                    angle = angles[self.mbqcircuit.trainable_nodes.index(i)]
                else:
                    angle = self.mbqcircuit[i].angle

                self.qstate, outcome = self.measure(angle, mode)
                self.outcomes[i] = outcome

        elif self.dev_mode:
            while self.current_measurement < len(self.schedule_measure):
                for node in self.current_simulated_nodes():
                    cond = False
                    futnods = self.future_neighbors_in_wire(node)
                    if len(futnods) == 0:
                        cond = True
                    else:
                        cond = futnods[0] in self.current_simulated_nodes()
                    if cond:
                        # current_ment = self.mbqcircuit[node].copy()
                        # indx = self.current_simulated_nodes().index(node)
                        break

                if cond == False:
                    raise ValueError("WTF")
                if node in self.mbqcircuit.trainable_nodes:
                    angle = angles[self.mbqcircuit.trainable_nodes.index(node)]
                    if isinstance(self.mbqcircuit[node], ControlledMent):
                        cond_angle = self.mbqcircuit[node].angle(self.outcomes) or angle
                        angle = cond_angle
                elif isinstance(self.mbqcircuit[node], Ment):
                    angle = self.mbqcircuit[node].angle

                self.qstate, outcome = self.measure(angle, mode)
                self.outcomes[node] = outcome

        current_output_order = [
            i for i in self.schedule if i not in self.schedule_measure
        ]
        if self.mbqcircuit.quantum_output_nodes != current_output_order:
            self.qstate = self.reorder_qubits(
                self.qstate, current_output_order, self.mbqcircuit.quantum_output_nodes
            )

        # # check if output nodes have a measurement, if so, measure them
        # for i in self.mbqcircuit.output_nodes:
        #     if isinstance(self.mbqcircuit[i], Ment):
        #         self.qstate, outcome = self.measure_ment(
        #             self.mbqcircuit[i], self.mbqcircuit[i].angle, i, force0=self.force0
        #         )
        #         self.outcomes[i] = outcome

        return self.qstate

    def reset(self, input_state: np.ndarray = None):
        """Resets the simulator to the initial state."""
        self.current_measurement = 0

        if input_state is not None:
            input_state = self.reorder_qubits(
                input_state,
                self.mbqcircuit.input_nodes,
                self.schedule[: len(self.mbqcircuit.input_nodes)],
            )
            self.input_state = input_state
            for i in range(self.window_size - len(self.mbqcircuit.input_nodes)):
                self.input_state = np.kron(self.input_state, qubit_plus)

        self.qstate = calc.pure2density(self.input_state)

        self.qstate = self.initial_czs @ self.qstate @ np.conj(self.initial_czs).T
        self.outcomes = {}

        if self.dev_mode:
            self._current_simulated_nodes = self.schedule[0 : self.window_size]

    def measure_ment(self, ment: Ment, angle, i, force0=False, mode="sample"):
        """
        Measures a ment
        """

        op = ment.matrix(angle, self.outcomes)
        if op is None:
            raise ValueError(f"Ment has no matrix representation at qubit {i}")

        p0, p1 = ment.get_povm(angle, self.outcomes)
        p0_extended = gates.arbitrary_qubit_gate(
            p0, i, self.current_number_simulated_nodes()
        )
        p1_extended = gates.arbitrary_qubit_gate(
            p1, i, self.current_number_simulated_nodes()
        )

        prob0 = np.real(np.trace(self.qstate @ p0_extended))
        prob1 = np.real(np.trace(self.qstate @ p1_extended))

        COND = (mode == "expectation" or mode == "exp") and ment.plane == "Z"

        if not force0 or ment.plane == "Z":
            if COND:
                outcome = prob1 / (prob0 + prob1)
            else:
                outcome = np.random.choice([0, 1], p=[prob0, prob1] / (prob0 + prob1))
        else:
            if prob0 < 1e-4:
                outcome = 1  # important when measuring Z's -- should make pretty
            else:
                outcome = 0

        if not COND:
            if outcome == 0:
                self.qstate = p0_extended @ self.qstate @ np.conj(p0_extended).T / prob0
            else:
                self.qstate = p1_extended @ self.qstate @ np.conj(p1_extended).T / prob1

        return self.qstate, outcome

    def find_swaps(self, source, target):
        assert set(source) == set(
            target
        ), f"Both lists must have the same elements, but source={source} and target={target}"

        swaps = []
        source = list(source)  # Make a copy to avoid modifying the original list

        for i, target_element in enumerate(target):
            if source[i] != target_element:
                j = source.index(target_element, i + 1)
                source[i], source[j] = source[j], source[i]  # Swap elements
                swaps.append((i, j))

        return swaps

    def reorder_qubits(self, state, current_order, target_order):
        """
        Reorders the qubits in the given order.
        """
        new_state = state.copy()
        type_state = "dm"
        if len(new_state.shape) == 1:
            type_state = "pure"

        swaps = self.find_swaps(current_order, target_order)
        for i, j in swaps:
            swap_op = gates.swap_ij(i, j, len(current_order))
            if type_state == "pure":
                new_state = swap_op @ new_state
            else:
                new_state = swap_op @ new_state @ np.conj(swap_op).T
        return new_state
