import numpy as np

def matrix_addition(A, B):
    """
    Adds two matrices A and B.

    Parameters:
    A (numpy.ndarray): First matrix.
    B (numpy.ndarray): Second matrix.

    Returns:
    numpy.ndarray: The sum of matrices A and B.
    """
    return np.add(A, B)

def matrix_subtraction(A, B):
    """
    Subtracts matrix B from matrix A.

    Parameters:
    A (numpy.ndarray): First matrix.
    B (numpy.ndarray): Second matrix.

    Returns:
    numpy.ndarray: The difference of matrices A and B.
    """
    return np.subtract(A, B)