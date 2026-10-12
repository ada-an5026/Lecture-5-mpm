import numpy as np

def matrix_multiply(A, B):
    """
    Multiplies two matrices A and B.

    Parameters:
    A (numpy.ndarray): First matrix.
    B (numpy.ndarray): Second matrix.

    Returns:
    numpy.ndarray: The product of matrices A and B.
    """
    return np.dot(A, B)

def element_wise_multiply(A, B):
    """
    Performs element-wise multiplication of two matrices A and B.

    Parameters:
    A (numpy.ndarray): First matrix.
    B (numpy.ndarray): Second matrix.

    Returns:
    numpy.ndarray: The element-wise product of matrices A and B.
    """
    return A*B
