import sys

import numpy as np
from matplotlib.collections import LineCollection


def to_contiguous_numpy_array(vec) -> np.ndarray:
    """Ensures the input vector is contiguous before passing it to a MeshKernel C API function,
     if the vector has been created with slicing operations.

    Args:
        vec (np.ndarray): The input vector.

    Returns:
        np.ndarray: The contiguous vector.

    Raises:
        TypeError: If `vec` is not a NumPy array.
    """
    if not isinstance(vec, np.ndarray):
        raise TypeError(
            "Input must be a NumPy array in to_contiguous_numpy_array function."
        )

    return np.ascontiguousarray(vec)


def plot_edges(node_x, node_y, edge_nodes, ax, *args, **kwargs):
    """Plots the edges at a given axes.
    `args` and `kwargs` will be used as parameters of the `plot` method.


    Args:
        node_x (ndarray): A 1D double array describing the x-coordinates of the nodes.
        node_y (ndarray): A 1D double array describing the y-coordinates of the nodes.
        edge_nodes (ndarray, optional): A 1D integer array describing the nodes composing each mesh 2d edge.
        ax (matplotlib.axes.Axes): The axes where to plot the edges
    """
    n_edge = int(edge_nodes.size / 2)
    edge_coords = np.empty((n_edge, 2, 2), dtype=np.float64)
    node_0 = edge_nodes[0::2]
    node_1 = edge_nodes[1::2]
    edge_coords[:, 0, 0] = node_x[node_0]
    edge_coords[:, 0, 1] = node_y[node_0]
    edge_coords[:, 1, 0] = node_x[node_1]
    edge_coords[:, 1, 1] = node_y[node_1]
    line_segments = LineCollection(edge_coords, *args, **kwargs)
    ax.add_collection(line_segments)
    ax.autoscale(enable=True)


def get_maximum_bounding_box_coordinates():
    """Get the maximum coordinate values for a bounding box defined by floating point coordinates"""

    x_lower_left = -sys.float_info.max
    y_lower_left = -sys.float_info.max

    x_upper_right = sys.float_info.max
    y_upper_right = sys.float_info.max

    return x_lower_left, y_lower_left, x_upper_right, y_upper_right
