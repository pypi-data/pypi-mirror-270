# Copyright 2023 Luis Mantilla
#
# Licensed under the Apache License, Version 2.0.
# See <http://www.apache.org/licenses/LICENSE-2.0> for details.
"""The graph_state module"""
import copy
from functools import cached_property, reduce
from typing import Optional, List, Tuple, Callable, Dict

import numpy as np
import scipy as scp
import networkx as nx
import matplotlib.pyplot as plt

from mentpy.operators import Ment, ControlMent
from mentpy.mbqc.states.graphstate import GraphState
from mentpy.mbqc.flow import Flow

__all__ = ["MBQCircuit", "merge", "hstack", "vstack"]


class MBQCircuit:
    r"""The MBQCircuit class that deals with operations and manipulations of graph states

    Parameters
    ----------
    graph: mp.GraphState
        The graph state of the MBQC circuit.
    input_nodes: list
        The input nodes of the MBQC circuit.
    output_nodes: list
        The output nodes of the MBQC circuit.
    measurements: dict
        The measurements of the MBQC circuit. The keys are the nodes and the values are the measurements.
    default_measurement: mp.Ment
        The default measurement of the MBQC circuit if no `measurements` are given.

    Examples
    --------
    Create a 1D cluster state :math:`|G>` of five qubits

    .. ipython:: python

        g = mp.GraphState()
        g.add_edges_from([(0,1), (1,2), (2,3), (3, 4)])
        state = mp.MBQCircuit(g, input_nodes=[0], output_nodes=[4])


    See Also
    --------
    :class:`mp.GraphState`

    Group
    -----
    mbqc
    """

    def __init__(
        self,
        graph: GraphState,
        input_nodes: List[int] = [],
        output_nodes: List[int] = [],
        measurements: Optional[Dict[int, Ment]] = None,
        default_measurement: Optional[Ment] = Ment("XY"),
        relabel_indices: bool = True,
    ) -> None:
        """Initializes a graph state"""

        if relabel_indices:
            graph, input_nodes, output_nodes, measurements = self._relabel_graph(
                graph, input_nodes, output_nodes, measurements
            )

        self._graph = graph
        self._setup_nodes(input_nodes, output_nodes)
        self._setup_measurements(measurements, default_measurement)
        self._update_attributes()

        # create flow
        self._flow = Flow(
            graph,
            input_nodes,
            output_nodes,
            {v: m.plane for v, m in self.measurements.items() if m is not None},
        )
        self._flow.initialize_flow()

        # Temporary fix for controlled nodes
        if self.partial_order is not None and self.controlled_nodes != []:
            old_partial_order = self._partial_order
            self._partial_order = _create_new_partial_order(
                self.controlled_nodes, self.measurements, old_partial_order
            )

        # In case we measure an output node
        quantum_output_nodes = [
            node for node, i in self.measurements.items() if i is None
        ]

        self._quantum_output_nodes = quantum_output_nodes
        self._measurement_order = None

    def _relabel_graph(
        self,
        graph: nx.Graph,
        input_nodes: List[int],
        output_nodes: List[int],
        measurements: Optional[Dict[int, "Ment"]],
    ) -> Tuple[nx.Graph, List[int], List[int], Optional[Dict[int, "Ment"]]]:
        """Relabels the graph nodes and updates related node indices.

        Args:
            graph (nx.Graph): The original graph.
            input_nodes (List[int]): Original input node indices.
            output_nodes (List[int]): Original output node indices.
            measurements (Optional[Dict[int, 'Ment']]): Original node measurements.

        Returns:
            tuple: A tuple containing the relabeled graph, input nodes, output nodes, and measurements.
        """
        N = graph.number_of_nodes()
        mapping = dict(zip(sorted(graph.nodes), range(N)))
        graph = nx.relabel_nodes(graph, mapping)
        input_nodes = [mapping[i] for i in input_nodes]
        output_nodes = [mapping[i] for i in output_nodes]
        if measurements is not None:
            measurements = {mapping[k]: v for k, v in measurements.items()}

        return graph, input_nodes, output_nodes, measurements

    def _setup_nodes(self, input_nodes: List[int], output_nodes: List[int]) -> None:
        """Setup the input and output nodes of the MBQCircuit"""
        if not all([v in self.graph.nodes for v in input_nodes]):
            raise ValueError(
                f"Input nodes {input_nodes} are not in the graph. Graph nodes are {self.graph.nodes}"
            )
        if not all([v in self.graph.nodes for v in output_nodes]):
            raise ValueError(
                f"Output nodes {output_nodes} are not in the graph. Graph nodes are {self.graph.nodes}"
            )

        self._input_nodes = input_nodes
        self._output_nodes = output_nodes

    def _setup_measurements(
        self, measurements: Dict[int, Ment], default_measurement: Ment
    ) -> None:
        """Setup the measurements of the MBQCircuit"""
        # Type check default_measurement
        if not isinstance(default_measurement, Ment):
            raise ValueError(
                f"Default measurement {default_measurement} is not an instance of Ment."
            )
        self._default_measurement = default_measurement

        # Type check measurements
        if measurements is None:
            measurements = {node: default_measurement for node in self.outputc}
            for node in self.output_nodes:
                measurements[node] = None
        else:
            if not all([v in self.graph.nodes for v in measurements.keys()]):
                nodes_not_in_graph = [
                    v for v in measurements.keys() if v not in self.graph.nodes
                ]
                raise ValueError(f"Nodes {nodes_not_in_graph} are not in the graph.")
            if not all(
                [isinstance(v, Ment) or v is None for v in measurements.values()]
            ):
                raise ValueError(
                    f"Values {measurements.values()} are not instances of Ment."
                )

            for node in self.graph.nodes:
                if node not in measurements:
                    measurements[node] = (
                        self._default_measurement if node in self.outputc else None
                    )

        self._measurements = measurements

    def __repr__(self) -> str:
        """Return the representation of the current MBQC circuit state"""
        return f"MBQCircuit with {self.graph.number_of_nodes()} qubits."

    def __len__(self) -> int:
        """Return the number of nodes in the MBQCircuit"""
        return len(self.graph)

    def __getattr__(self, name):
        # If the attribute is not found in the MBQCircuit, try to find it in the graph or flow
        try:
            return getattr(self.graph, name)
        except AttributeError:
            try:
                return getattr(self._flow, name)
            except AttributeError:
                raise AttributeError(f"Attribute {name} not found in MBQCircuit.")

    def __setitem__(self, key, value):
        r"""Set the value of the measurement of the node with index key."""
        if key not in self.graph.nodes:
            raise ValueError(f"Node {key} is not in the graph.")
        if not isinstance(value, Ment):
            raise ValueError(f"Value {value} is not a Measurement object.")

        self._measurements[key] = value

        # self._update_attributes_key(key)
        self._update_attributes()

        if isinstance(value, ControlMent):
            # recalculate measurement order
            self._measurement_order = self.calculate_order()

    def __getitem__(self, key):
        r"""Return the value of the measurement of the node with index key."""
        try:
            return self._measurements[key]
        except KeyError:
            raise ValueError(f"Node {key} is not in the graph.")

    def __delitem__(self, key):
        """Delete the measurement of the node with index key."""

        if key not in self.graph.nodes:
            raise ValueError(f"Node {key} is not in the graph.")

        self._measurements[key] = None

    @property
    def measurements(self) -> Dict[int, Ment]:
        r"""Return the measurements of the MBQC circuit."""
        return self._measurements

    @measurements.setter
    def measurements(self, measurements: Dict[int, Ment]) -> None:
        r"""Set the measurements of the MBQC circuit."""
        if not all([v in self.graph.nodes for v in measurements.keys()]):
            raise ValueError(f"Nodes {measurements.keys()} are not in the graph.")
        if not all([isinstance(v, Ment) for v in measurements.values()]):
            raise ValueError(
                f"Values {measurements.values()} are not Measurement objects."
            )
        self._measurements = measurements
        self._update_attributes()

    @property
    def graph(self) -> GraphState:
        r"""Return the graph of the resource state."""
        return self._graph

    @property
    def input_nodes(self) -> List[int]:
        r"""Return the input nodes of the MBQC circuit."""
        return self._input_nodes

    @property
    def output_nodes(self) -> List[int]:
        r"""Return the output nodes of the MBQC circuit."""
        return self._output_nodes

    @property
    def quantum_output_nodes(self) -> List[int]:
        r"""Return the output nodes of the MBQC circuit."""
        return self._quantum_output_nodes

    @property
    def classical_output_nodes(self) -> List[int]:
        r"""Return the output nodes of the MBQC circuit."""
        return self._classical_output_nodes

    @property
    def trainable_nodes(self) -> List[int]:
        r"""Return the trainable nodes of the MBQC circuit."""
        return self._trainable_nodes

    @trainable_nodes.setter
    def trainable_nodes(self, trainable_nodes: List[int]) -> None:
        r"""Set the trainable nodes of the MBQC circuit."""
        if not all([v in self.graph.nodes for v in trainable_nodes]):
            raise ValueError(
                f"Trainable nodes {trainable_nodes} are not in the graph. Graph nodes are {self.graph.nodes}"
            )
        self._trainable_nodes = trainable_nodes

    @property
    def controlled_nodes(self) -> List[int]:
        r"""Return the controlled nodes of the MBQC circuit."""
        return self._controlled_nodes

    @property
    def flow(self) -> Flow:
        r"""Return the flow function of the MBQC circuit."""
        return self._flow

    @property
    def partial_order(self) -> Callable:
        r"""Return the partial order function of the MBQC circuit."""
        return self._flow.partial_order

    @property
    def depth(self) -> int:
        r"""Return the depth of the MBQC circuit."""
        return self._flow.depth

    @property
    def measurement_order(self) -> List[int]:
        r"""Return the measurement order of the MBQC circuit."""
        if self._flow.flow_initialized is False:
            self._flow.initialize_flow()
        if self._measurement_order is None:
            self._measurement_order = self.calculate_order()

        return self._measurement_order

    @measurement_order.setter
    def measurement_order(self, measurement_order: List[int]) -> None:
        r"""Set the measurement order of the MBQC circuit."""
        if not _check_measurement_order(measurement_order, self.partial_order):
            raise ValueError(f"Invalid measurement order {measurement_order}.")
        self._measurement_order = measurement_order

    @cached_property
    def outputc(self) -> List:
        r"""Returns :math:`O^c`, the complement of output nodes."""
        return [v for v in self.graph.nodes() if v not in self.output_nodes]

    @cached_property
    def inputc(self) -> List:
        r"""Returns :math:`I^c`, the complement of input nodes."""
        return [v for v in self.graph.nodes() if v not in self.input_nodes]

    def ordered_layers(self, train_indices=False) -> List[List[int]]:
        r"""Returns the layers of the MBQC circuit."""
        if self._flow.func is None:
            return None
        if train_indices:
            # return the nested layers in Flow.layers but with the trainable_nodes indices
            return [
                [self.trainable_nodes.index(node) for node in layer]
                for layer in self._flow.layers[:-1]
            ]
        return self._flow.layers

    def _update_attributes(self) -> None:
        trainable_nodes = []
        controlled_nodes = []
        quantum_outputs = []
        classical_outputs = []

        for nodei, menti in self._measurements.items():
            if menti is not None:
                if isinstance(menti, ControlMent):
                    controlled_nodes.append(nodei)

                if menti.is_trainable():
                    trainable_nodes.append(nodei)

                self._measurements[nodei] = copy.deepcopy(menti)
                self._measurements[nodei].node_id = nodei
                if nodei in self._output_nodes:
                    classical_outputs.append(nodei)
            else:
                if nodei in self._output_nodes:
                    quantum_outputs.append(nodei)

        self._trainable_nodes = trainable_nodes
        self._controlled_nodes = controlled_nodes
        self._quantum_output_nodes = quantum_outputs
        self._classical_output_nodes = classical_outputs

        # update measurement order

        # make artificial graph for new flow with controls
        # if len(self.controlled_nodes) > 0:
        #     artificial_graph = self.graph
        #     for nodei in self.controlled_nodes:
        #         new_edges = [(nodei, v) for v in self.measurements[nodei].condition.cond_nodes]
        #         artificial_graph.add_edges_from(new_edges)

        #     flow, partial_order, depth = find_cflow(artificial_graph, self.input_nodes, self.output_nodes)
        #     self._flow = flow
        #     self._partial_order = partial_order
        #     self._depth = depth

    def _update_attributes_key(self, key) -> None:
        menti = self._measurements[key]
        if menti is not None:
            if menti.angle is None and key not in self._trainable_nodes:
                self._trainable_nodes.append(key)
            elif menti.angle is not None and key in self._trainable_nodes:
                self._trainable_nodes.remove(key)
            self._measurements[key] = copy.deepcopy(menti)
            self._measurements[key].node_id = key
        else:
            if key in self._trainable_nodes:
                self._trainable_nodes.remove(key)

    def calculate_order(self):
        r"""Returns the order of the measurements"""
        n = len(self.graph)
        mat = np.zeros((n, n), dtype=int)

        for indi, i in enumerate(list(self.graph.nodes())):
            for indj, j in enumerate(list(self.graph.nodes())):
                if self._flow.partial_order(i, j):
                    mat[indi, indj] = 1

        sum_mat = np.sum(mat, axis=1)
        order = np.argsort(sum_mat)[::-1]

        sum_dict = {}
        for i, s in enumerate(sum_mat):
            if s not in sum_dict:
                sum_dict[s] = []
            sum_dict[s].append(i)
        sorted_indices = [
            sum_dict[key] for key in sorted(sum_dict.keys(), reverse=True)
        ]
        sorted_labels = [
            [list(self.graph.nodes())[i] for i in group] for group in sorted_indices
        ]
        self._sorted_labels = sorted_labels

        order = [item for sublist in sorted_labels for item in sublist]

        for i in self.input_nodes[::-1]:
            order.remove(i)
            order.insert(0, i)

        return order

    def add_edge(self, u, v):
        r"""Adds an edge between nodes u and v"""
        self.graph.add_edge(u, v)
        # try resetting self with new graph, if it fails, remove the edge
        try:
            self.__init__(self.graph, self.input_nodes, self.output_nodes)
        except Exception as e:
            self.graph.remove_edge(u, v)
            raise ValueError(f"Cannot add edge between {u} and {v}.\n" + str(e))

    def add_edges_from(self, edges, **kwargs):
        r"""Adds edges from a list of tuples"""
        new_graph = self.graph.copy()
        new_graph.add_edges_from(edges, **kwargs)
        try:
            self.__init__(
                new_graph,
                self.input_nodes,
                self.output_nodes,
            )
        except Exception as e:
            raise ValueError(f"Cannot add edges {edges}.\n" + str(e))


def _check_measurement_order(measurement_order: List, partial_order: Callable):
    r"""Checks that the measurement order is valid"""
    for i in range(len(measurement_order)):
        for j in range(i + 1, len(measurement_order)):
            if partial_order(measurement_order[i], measurement_order[j]):
                return False
    return True


def merge(state1: MBQCircuit, state2: MBQCircuit, along=[]) -> MBQCircuit:
    """Merge two MBQC circuits into a larger MBQC circuit. This is, the input and
    output of the new MBQC circuit will depend on the concat_indices.

    Group
    -----
    mbqc
    """

    for i, j in along:
        if i not in state1.output_nodes or j not in state2.input_nodes:
            raise ValueError(f"Cannot merge states at indices {i} and {j}")

    graph = nx.disjoint_union(state1.graph, state2.graph)
    along1, along2 = zip(*along)

    input_nodes = state1.input_nodes + [
        i + len(state1.graph) for i in state2.input_nodes if i not in along2
    ]
    output_nodes = []
    added_ind = []
    for j in state1.output_nodes:
        if j in along1:
            output_ind = along1.index(j)
            inputnode = along2[output_ind]
            input_index = state2.input_nodes.index(inputnode)
            added_ind.append(input_index)
            output_nodes.append(state2.output_nodes[input_index] + len(state1.graph))
        else:
            output_nodes.append(j)
    output_nodes += [
        i + len(state1.graph)
        for indx, i in enumerate(state2.output_nodes)
        if indx not in added_ind
    ]

    measurements = dict(state1.measurements)
    measurements.update(
        {i + len(state1.graph): ment for i, ment in state2.measurements.items()}
    )

    for i, j in along:
        graph.add_edge(i, j + len(state1.graph))
        graph = nx.contracted_edge(graph, (j + len(state1.graph), i), self_loops=False)
        del measurements[i]

    return MBQCircuit(graph, input_nodes, output_nodes, measurements=measurements)


def vstack(states) -> MBQCircuit:
    """Vertically stack a list of graph states into a larger graph state. This is,
    the input of the new MBQC circuit is the input of the first state, and the output
    is the output of the last state.

    Group
    -----
    mbqc
    """
    if len(states) == 0:
        raise ValueError("Cannot vertically stack an empty list of states.")
    if len(states) == 1:
        return states[0]
    return reduce(_vstack2, states)


def hstack(states) -> MBQCircuit:
    """Horizontally stack a list of graph states into a larger graph state. This is,
    the input of the new MBQC circuit is the input of the first state, and the output
    is the output of the last state.

    Group
    -----
    mbqc
    """
    if len(states) == 0:
        raise ValueError("Cannot horizontally stack an empty list of states.")
    if len(states) == 1:
        return states[0]
    return reduce(_hstack2, states)


def _vstack2(state1: MBQCircuit, state2: MBQCircuit) -> MBQCircuit:
    """Vertically stack two graph states into a larger graph state. This is,
    the input of the new MBQC circuits is both the input of the first and second
    state, and the output is the output of the first and second state.

    Group
    -----
    mbqc
    """
    graph = nx.disjoint_union(state1.graph, state2.graph)
    input_nodes = state1.input_nodes + [
        i + len(state1.graph) for i in state2.input_nodes
    ]
    output_nodes = state1.output_nodes + [
        i + len(state1.graph) for i in state2.output_nodes
    ]

    measurements = dict(state1.measurements)
    measurements.update(
        {i + len(state1.graph): plane for i, plane in state2.measurements.items()}
    )

    # TODO: Compute flow and partial order
    return MBQCircuit(graph, input_nodes, output_nodes, measurements=measurements)


def _hstack2(state1: MBQCircuit, state2: MBQCircuit) -> MBQCircuit:
    """Horizontally stack two graph states into a larger graph state. This is,
    the input of the new MBQC circuit is the input of the first state, and the
    output is the output of the second state.

    Args
    ----
    state1: MBQCircuit
        The first state to stack.
    state2: MBQCircuit
        The second state to stack.

    Group
    -----
    mbqc
    """
    # check that the size of the output of the first state is the same as the
    # size of the input of the second state
    if len(state1.output_nodes) != len(state2.input_nodes):
        raise ValueError(
            "The output of the first state must be the same size as the input "
            "of the second state."
        )

    # create new graph
    graph = nx.disjoint_union(state1.graph, state2.graph)

    nodes1 = list(state1.graph.nodes())
    nodes2 = list(state2.graph.nodes())

    for i in range(len(state1.output_nodes)):
        graph.add_edge(
            nodes1.index(state1.output_nodes[i]),
            nodes2.index(state2.input_nodes[i]) + len(nodes1),
        )

    input_nodes = [nodes1.index(i) for i in state1.input_nodes]
    output_nodes = [nodes2.index(j) + len(nodes1) for j in state2.output_nodes]

    measurements = {nodes1.index(i): ment for i, ment in state1.measurements.items()}
    measurements.update(
        {nodes2.index(i) + len(nodes1): ment for i, ment in state2.measurements.items()}
    )

    for i, j in zip(state1.output_nodes, state2.input_nodes):
        graph.add_edge(i, j + len(state1.graph))
        graph = nx.contracted_edge(graph, (j + len(state1.graph), i), self_loops=False)
        del measurements[i]

    # TODO: Compute flow and partial order
    return MBQCircuit(graph, input_nodes, output_nodes, measurements=measurements)


def _create_new_partial_order(controlled_nodes, measurements, old_partial_order):
    def new_partial_order(i, j):
        for c in controlled_nodes:
            cns = measurements[c].condition.cond_nodes

            ibeforecns = any([old_partial_order(i, cn) for cn in cns]) or i in cns
            jafterc = old_partial_order(c, j) or j == c
            # print(f"Comparing {i} and {j}")
            # print(any([old_partial_order(i, cn) for cn in cns]), i in cns)
            # print(old_partial_order(c, j), j == c)
            if ibeforecns and jafterc and i != j:
                return True

            if j in cns and i == c:
                return False

        return old_partial_order(i, j)

    return new_partial_order
