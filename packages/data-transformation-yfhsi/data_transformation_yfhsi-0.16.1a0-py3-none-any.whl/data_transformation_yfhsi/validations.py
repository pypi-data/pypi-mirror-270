import numpy as np

"""
The file contains validation functions for data transformation
library functions.
"""


def validate_transpose2d_matrix(input_matrix: any) -> bool:
    """
    Validates the input matrix of the transpose2d function.

    Parameters:
        input_matrix (any): The matrix to be validated.

    Returns:
        bool: True if the matrix is valid.
    """
    if isinstance(input_matrix, list):
        if all(isinstance(row, list) for row in input_matrix):
            if all(
                isinstance(item, float) for row in input_matrix for item in row
            ):
                if all(
                    len(input_matrix[0]) == len(row) for row in input_matrix
                ):
                    return True
                else:
                    raise ValueError("The matrix has an inhomogeneous shape.")
            else:
                raise ValueError(
                    "All matrix items must be floating-point numbers."
                )
        else:
            raise ValueError("The submitted matrix is not 2D.")
    else:
        raise ValueError("The submitted matrix is not a list.")


def validate_window1d_matrix(input_array: any) -> bool:
    """
    Validates the input matrix of the window1d function.

    Parameters:
        input_array (any): The matrix to be validated.

    Returns:
        bool: True if the matrix is valid.
    """
    if np.array(input_array).ndim == 1:
        if isinstance(input_array, list) or isinstance(
            input_array, np.ndarray
        ):
            if all(np.isreal(item) for item in input_array):
                return True
            else:
                raise ValueError("All matrix items must be real numbers.")
        else:
            raise ValueError("Submitted matrix is not list or np.ndarray.")
    else:
        raise ValueError("Submitted matrix is not 1D.")


def validate_convolution2d_matrix(input_matrix: any) -> bool:
    """
    Validates the input matrix of the convolution2d function.

    Parameters:
        input_array (any): The matrix to be validated.

    Returns:
        bool: True if the matrix is valid.
    """
    if np.array(input_matrix).ndim == 2:
        if isinstance(input_matrix, np.ndarray):
            if all(np.isreal(item) for row in input_matrix for item in row):
                return True
            else:
                raise ValueError("All matrix items must be real numbers.")
        else:
            raise ValueError("Submitted matrix is not np.ndarray.")
    else:
        raise ValueError("Submitted matrix is not 2D.")


def function_variables_verification(variable: any) -> bool:
    """
    The function verifies whether data transformation functions
    variables are positive numbers.

    Parameters:
        variable (any): The function variable to be validated.

    Returns:
        bool: True if the function varible is valid.
    """
    if isinstance(variable, int):
        if variable > 0:
            return True
        else:
            raise ValueError("The function variable must be positive number.")
    else:
        raise ValueError("The function variable must be integer number.")
