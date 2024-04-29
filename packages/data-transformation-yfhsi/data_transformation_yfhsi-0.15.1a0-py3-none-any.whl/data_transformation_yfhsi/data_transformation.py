import logging

import numpy as np
from validations import (
    function_variables_verification,
    validate_convolution2d_matrix,
    validate_transpose2d_matrix,
    validate_window1d_matrix,
)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


def transpose2d(input_matrix: list[list[float]]) -> list:
    """
    The transpose function for a 2D matrix.

    Parameters:
        input_matrix (list[list[float]]): The input 2D matrix to be transposed.

    Returns:
        list: The transposed 2D matrix.
    """
    try:
        validate_transpose2d_matrix(input_matrix)

        transposed_matrix = []
        for column_index in range(len(input_matrix[0])):
            column = [row[column_index] for row in input_matrix]
            transposed_matrix.append(column)

        return transposed_matrix

    except Exception as error:
        logging.error(error)

        return "The function has failed."


def window1d(
    input_array: list | np.ndarray, size: int, shift: int = 1, stride: int = 1
) -> list[list | np.ndarray]:
    """
    The time series windowing function for 1D matrix or numpy array.

    Parameters:
        input_array (list | np.ndarray): The input 1D array or numpy array.
        size (int): The size of the sliding window.
        shift (int): The amount to shift the window by for each step.
        Default is 1.
        stride (int): The stride of the window.
        Default is 1.

    Returns:
        list[list | np.ndarray]: A list of windows,
        each containing elements from the input array.
    """
    try:
        validate_window1d_matrix(input_array)

        function_variables_verification(size)
        function_variables_verification(shift)
        function_variables_verification(stride)

        windows = []
        for index in range(0, len(input_array), shift):
            window = input_array[index:index + size * stride:stride]
            if len(window) == size:
                windows.append(window)

        if isinstance(input_array, list):
            return windows
        elif isinstance(input_array, np.ndarray):
            return np.array(windows)

    except Exception as error:
        logging.error(error)

        return "The function has failed."


def convolution2d(
    input_matrix: np.ndarray, kernel: np.ndarray, stride: int = 1
) -> np.ndarray:
    """
    The cross correlation function between a 2D input matrix and a 2D kernel.

    Parameters:
        input_matrix (np.ndarray): The input 2D matrix.
        kernel (np.ndarray): The 2D convolution kernel.
        stride (int): The stride of the convolution operation. Default is 1.

    Returns:
        np.ndarray: The result of the 2D convolution operation.
    """
    try:
        validate_convolution2d_matrix(input_matrix)
        validate_convolution2d_matrix(kernel)

        function_variables_verification(stride)

        matrix_rows, matrix_columns = len(input_matrix), len(input_matrix[0])
        kernel_rows, kernel_columns = len(kernel), len(kernel[0])
        width, height = (
            (matrix_rows - kernel_rows) // stride + 1,
            (matrix_columns - kernel_columns) // stride + 1,
        )

        output_matrix = np.zeros((width, height))
        for column in range(0, matrix_columns - kernel_columns + 1, stride):
            for row in range(0, matrix_rows - kernel_rows + 1, stride):
                window = input_matrix[
                    row:row + kernel_rows, column:column + kernel_columns
                ]
                value = np.sum(window * kernel)
                output_matrix[row // stride, column // stride] = value

        return output_matrix

    except Exception as error:
        logging.error(error)

        return "The function has failed."
