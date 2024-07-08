import numpy as np


def shuffle_by_1(A):
    """
    Shuffles the columns of a matrix to the right by one.

    This function returns the matrix A with columns shuffled to the right by 1,
    such that the new ith col is the old i-1th col, and the new 1st col
    is the old last col.
    """
    n = A.shape[1]
    # Stack last column at the front
    columns, last_column = np.hsplit(A, (n - 1,))
    return np.hstack((last_column, columns))


rng = np.random.default_rng(seed=181)
A = rng.standard_normal((2, 3))
print(f"A is\n {A} \nResult of `shuffle_by_1` is\n {shuffle_by_1(A)}")
