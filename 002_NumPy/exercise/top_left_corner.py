import numpy as np


def top_left_corner(A, r, c):
    """
    Select the top-left corner of a (m x n) matrix.

    This function returns the r-by-c top-left corner of the matrix A
    """
    m = A.shape[0]
    n = A.shape[1]
    if r > m or c > n:
        raise ValueError(f"Can't select {r}x{c} matrix from a {m}x{n} matrix.")

    # Choose r-rows
    rows_matrix = A[0:r]
    # Choose c-columns of rows matrix
    B = np.transpose(rows_matrix)[0:c]

    return np.transpose(B)


rng = np.random.default_rng(seed=3942)
A = rng.standard_normal((4, 5))
r, c = 1, 2
result = top_left_corner(A, r, c)
print(f"A is\n {A} \nResult of {r}x{c} `top_left_corner` is\n {result}")
assert result.shape == (r, c)
