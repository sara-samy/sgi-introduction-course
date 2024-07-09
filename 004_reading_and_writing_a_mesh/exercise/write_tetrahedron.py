import gpytoolbox as gpy
import numpy as np
import os
import polyscope as ps


def write_tetrahedron():
    """
    Writes a tetrahedron to the file "tetrahedron.obj"
    """
    V = np.array([[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
    F = np.array([[1, 0, 2], [0, 1, 3], [1, 2, 3], [2, 0, 3]])
    return V, F


current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(current_directory)
data_directory = os.path.join(parent_directory, "data")

filename = "tetrahedron.obj"

ps.init()
V, F = write_tetrahedron()
ps.register_surface_mesh("tetrahedron", V, F)
ps.register_point_cloud("vertices", V)
gpy.write_mesh(os.path.join(data_directory, filename), V, F)
ps.show()
