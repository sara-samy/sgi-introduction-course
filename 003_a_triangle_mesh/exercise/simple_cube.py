import numpy as np
import polyscope as ps


def simple_cube():
    """Construct a triangle mesh for a single cube.

    This function returns two variables, the vertex-list V and the face-list
    F describing a triangle mesh of a single cube.
    """

    V = np.array(
        [
            [0.0, 0.0, 0.0],
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [1.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
            [1.0, 0.0, 1.0],
            [0.0, 1.0, 1.0],
            [1.0, 1.0, 1.0],
        ]
    )

    F = np.array(
        [
            [0, 2, 3, 1],
            [0, 2, 6, 4],
            [0, 4, 5, 1],
            [1, 5, 7, 3],
            [4, 5, 7, 6],
            [2, 3, 7, 6],
        ]
    )

    return V, F


V, F = simple_cube()
ps.init()
ps.register_surface_mesh("Cube", V, F)
ps.show()
