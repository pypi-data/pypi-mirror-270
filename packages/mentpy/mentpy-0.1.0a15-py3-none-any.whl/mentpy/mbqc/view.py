# Copyright 2023 Luis Mantilla
#
# Licensed under the Apache License, Version 2.0.
# See <http://www.apache.org/licenses/LICENSE-2.0> for details.
"""A module for drawing MBQC circuits."""

from typing import Union, Tuple

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


from mentpy.mbqc.mbqcircuit import MBQCircuit
from mentpy.mbqc.states.graphstate import GraphState

import warnings

__all__ = ["draw", "draw_with_wires"]

DEFAULT_NODE_COLOR = "#FFBD59"
INPUT_NODE_COLOR = "#ADD8E6"
OUTPUT_NODE_COLOR = "#ADD8E6"
CONTROLLED_NODE_COLOR = "#A88FE8"
UNTRAINABLE_NODE_COLOR = "#CCCCCC"


def get_node_colors(state, style="default"):
    """Return node colors based on the state and style."""

    possible_styles = ("default", "black_and_white", "blue_inputs")
    assert style in possible_styles, f"Style must be one of {possible_styles}"

    node_colors = {}

    # Base Coloring
    for i in state.graph.nodes():
        if i in state.controlled_nodes:
            node_colors[i] = CONTROLLED_NODE_COLOR
        elif i in state.quantum_output_nodes:
            node_colors[i] = OUTPUT_NODE_COLOR
        elif i in set(state.nodes()) - set(state.trainable_nodes):
            node_colors[i] = UNTRAINABLE_NODE_COLOR
        else:
            node_colors[i] = DEFAULT_NODE_COLOR

    # Style-based Adjustments
    if style == "black_and_white":
        node_colors = {i: "#FFFFFF" for i in state.graph.nodes()}
    elif style == "blue_inputs":
        for i in state.input_nodes:
            node_colors[i] = INPUT_NODE_COLOR

    return node_colors


def get_options(kwargs) -> dict:
    """Returns default options updated with user-defined values."""
    default_options = {
        "node_color": "white",
        "font_family": "Dejavu Sans",
        "font_weight": "medium",
        "font_size": 10,
        "edgecolors": "k",
        "node_size": 500,
        "edge_color": "grey",
        "edge_color_control": "#CCCCCC",
        "with_labels": True,
        "label": "indices",
        "transparent": True,
        "figsize": (8, 3),
        "show_controls": True,
        "show_flow": True,
        "pauliop": None,
        "style": "default",
        "position": None,
    }

    # Update default options with any provided by the user
    default_options.update(kwargs)

    return default_options


def draw(state: Union[MBQCircuit, GraphState], **kwargs) -> Tuple[plt.Figure, plt.Axes]:
    """Draws mbqc circuit with flow.

    Group
    -----
    mbqc
    """

    options = get_options(kwargs)

    show_controls = options.pop("show_controls")
    show_flow = options.pop("show_flow")
    pauliop = options.get("pauliop", None)
    edge_color_control = options.pop("edge_color_control")
    style = options.pop("style")
    position = options.pop("position")

    if pauliop is not None:
        if len(pauliop) != 1:
            raise ValueError("pauliop must be a single Pauli operator")
        options["label"] = "pauliop"

    if "labels" not in options:
        options["labels"] = process_labels(state, options)
    else:
        options.pop("pauliop")

    transp = options.pop("transparent")
    fig, ax = plt.subplots(figsize=options.pop("figsize"))

    if transp:
        fig.patch.set_alpha(0)
        ax.patch.set_alpha(0)

    if isinstance(state, GraphState):
        nx.draw(state, position, ax=ax, **options)

    elif isinstance(state, MBQCircuit):
        if state.flow is None:
            nx.draw(state.graph, position, ax=ax, **options)
        elif state.flow.name.lower() == "cflow":
            plt.close(fig)
            return draw_with_wires(state, **kwargs)
        else:
            layers = state.flow.layers
            node_colors = get_node_colors(state, style=style)
            options["node_color"] = [node_colors[node] for node in state.graph.nodes()]

            position_xy = {}
            for i, layer in enumerate(layers):
                for j, node in enumerate(layer):
                    position_xy[node] = (i, -j)

            nx.draw(state.graph, ax=ax, pos=position_xy, **options)

            if show_flow:
                nx.draw(_graph_with_flow(state), pos=position_xy, ax=ax, **options)

            if show_controls:
                dashed_edges = []
                for node in state.controlled_nodes:
                    for k in state.measurements[node].condition.cond_nodes:
                        dashed_edges.append((node, k))
                nx.draw_networkx_edges(
                    state.graph,
                    pos=position_xy,
                    edge_color=edge_color_control,
                    width=1.5,
                    edgelist=dashed_edges,
                    style="dashed",
                )

    return fig, ax


def draw_with_wires(
    state: Union[MBQCircuit, GraphState], fix_wires=None, **kwargs
) -> Tuple[plt.Figure, plt.Axes]:
    """Draws mbqc circuit with flow.

    TODO: Add support for graphs without flow, but with gflow
    TODO: Improve fix when there are control nodes

    Group
    -----
    mbqc
    """
    options = get_options(kwargs)

    show_controls = options.pop("show_controls")
    show_flow = options.pop("show_flow")
    pauliop = options.get("pauliop", None)
    edge_color_control = options.pop("edge_color_control")
    style = options.pop("style")
    position = options.pop("position")

    if pauliop is not None:
        if len(pauliop) != 1:
            raise ValueError("pauliop must be a single Pauli operator")
        options["label"] = "pauliop"

    if "labels" not in options:
        options["labels"] = process_labels(state, options)
    else:
        options.pop("pauliop")

    transp = options.pop("transparent")
    fig, ax = plt.subplots(figsize=options.pop("figsize"))

    if transp:
        fig.patch.set_alpha(0)
        ax.patch.set_alpha(0)

    if fix_wires is None and isinstance(state, MBQCircuit):
        if state.flow.name.lower() != "cflow":
            raise ValueError("Only cflow is supported at the moment")
        if state.flow is not None:
            fix_wires = []
            for inp in state.input_nodes:
                is_output = False
                wire = [inp]
                while not is_output:
                    out = state.flow(wire[-1])
                    wire.append(out)
                    if out in state.output_nodes:
                        is_output = True
                fix_wires.append(tuple(wire))

    if isinstance(state, GraphState):
        nx.draw(state, position, ax=ax, **options)

    elif isinstance(state, MBQCircuit):
        node_color = options.pop("node_color")
        if node_color is None:
            node_color = get_node_colors(state, style=style)
        node_colors = get_node_colors(state, style=style)
        options["node_color"] = [node_colors[node] for node in state.graph.nodes()]

        fixed_nodes = state.input_nodes + state.output_nodes
        position_xy = {}
        for indx, p in enumerate(state.input_nodes):
            position_xy[p] = (0, -1 * indx)

        separation = len(state.outputc) // len(state.output_nodes)
        if fix_wires is not None:
            for wire in fix_wires:
                if len(wire) + 2 > separation:
                    separation = len(wire) + 2
        for indx, p in enumerate(state.output_nodes):
            position_xy[p] = (2 * (separation) - 2, -1 * indx)

        if fix_wires is not None:
            x = [list(x) for x in fix_wires]

            fixed_nodes += sum(x, [])

            for indw, wire in enumerate(fix_wires):
                for indx, p in enumerate(wire):
                    if p != "*":
                        position_xy[p] = (2 * (indx + 1), -1 * indw)

        # remove all '*' from fixed_nodes
        fixed_nodes = [x for x in fixed_nodes if x != "*"]

        node_pos = nx.spring_layout(
            state.graph, pos=position_xy, fixed=fixed_nodes, k=1 / len(state.graph)
        )

        nx.draw(state.graph, ax=ax, pos=node_pos, **options)
        if state.flow is not None and show_flow:
            nx.draw(_graph_with_flow(state), pos=node_pos, ax=ax, **options)
        if show_controls:
            dashed_edges = []
            for node in state.controlled_nodes:
                for k in state.measurements[node].condition.cond_nodes:
                    dashed_edges.append((node, k))
            nx.draw_networkx_edges(
                state.graph,
                pos=node_pos,
                edge_color=edge_color_control,
                width=1.5,
                edgelist=dashed_edges,
                style="dashed",
            )

    return fig, ax


def process_labels(state: Union[MBQCircuit, GraphState], options: dict):
    """Process and return the appropriate labels for the nodes based on the given options."""

    label_option = options.pop("label", "index")
    pauliop = options.pop("pauliop", None)

    if label_option in ("index", "indices"):
        return None  # No modification necessary
    elif label_option in ("plane", "planes"):
        labels = {
            node: ("" if state[node] is None else state[node].plane)
            for node in state.graph.nodes()
        }
        for node in state.controlled_nodes:
            labels[node] = "Ctrl"
        return labels
    elif label_option in ("arrow", "arrows"):
        plane2arrow = {
            "X": r"$\uparrow$",
            "Y": r"$\rightarrow$",
            "XY": r"$\nearrow$",
            "Z": r"$\cdot$",
            "XZ": r"$\nwarrow$",
            "YZ": r"$\nwarrow$",
            "XYZ": r"$\nwarrow \nearrow$",
            "": "",
        }
        labels = {
            node: plane2arrow[("" if state[node] is None else state[node].plane)]
            for node in state.graph.nodes()
        }
        for node in state.controlled_nodes:
            labels[node] = "Ctrl"
        return labels
    elif label_option in ("angles", "angle"):
        labels = {}
        for node in state.graph.nodes():
            if state.measurements[node] is not None:
                if state.measurements[node].angle is not None:
                    labels[node] = round(state.measurements[node].angle, 3)
                else:
                    labels[node] = r"$\theta$"
            else:
                labels[node] = ""
        return labels
    elif label_option == "pauliop":
        obj_nodes = (
            state.graph.nodes() if isinstance(state, MBQCircuit) else state.nodes()
        )
        labels = {node: pauliop.txt[node] for node in obj_nodes}
        return labels
    else:
        raise ValueError(
            f"label must be one of ['index', 'plane', 'arrow', 'angles', 'pauliop'], not {label_option}"
        )


def _graph_with_flow(state):
    """Return digraph with flow (but does not have all CZ edges!)"""
    if state.flow.name.lower() != "cflow":
        return state.graph
    g = state.graph
    dflow = nx.DiGraph()
    dflow.add_nodes_from(g.nodes())
    for node in state.outputc:
        next_nodes = state.flow(node)
        vs = []
        if isinstance(next_nodes, int):
            vs = [next_nodes]
        else:
            # check indx where the flow is 1
            vs = [i for i, x in enumerate(next_nodes) if x == 1]

        for v in vs:
            dflow.add_edge(node, v)
    return dflow
