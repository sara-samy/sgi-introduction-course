import gpytoolbox as gpy, polyscope as ps, numpy as np
import os


def plot_z_coord(V):
    """This method plots the z-cordinate on the input mesh V,F"""
    # function = lambda row: row[2]
    # return np.apply_along_axis(function, 1, V)
    return V[:,2]


def norm(V):
    # V is (n x 3)-matrix
    # for each row (i.e. for each vertex), we want one scalar value
    # f should return (1 x n)-vector
    function = lambda row: np.linalg.norm(row)
    return np.apply_along_axis(function, 1, V)


current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(current_directory)
data_directory = os.path.join(parent_directory, "data")

# Initialize polyscope
ps.set_up_dir("z_up")
ps.set_front_dir("neg_y_front")
ps.set_navigation_style("free")

ps.init()
# notes:
# must pass `fmt` with starting `.`, if not `None`
# absolute path works fine
format = ".obj"
filename = "spot"
V, F = gpy.read_mesh(  # pyright: ignore
    os.path.join(data_directory, filename + format), fmt=format
)
ps_spot = ps.register_surface_mesh(filename, V, F)
f = plot_z_coord
f_values = f(V)
assert f_values.shape == (V.shape[0],)  # pyright: ignore
ps_spot.add_scalar_quantity(
    name="f", values=f_values, defined_on="vertices", enabled=True
)
ps.show()

