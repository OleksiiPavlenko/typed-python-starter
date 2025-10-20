"""Utility functions for common operations and mathematical calculations.

This module provides reusable utility functions that can be used throughout
the application for common calculations, data transformations, and matrix operations.
"""

from __future__ import annotations

from typing import Iterable

from .models import User, Matrix


def calculate_total(prices: Iterable[float]) -> float:
    """Calculate the total sum of a collection of prices.
    
    Takes an iterable of numeric values and returns their sum as a float.
    This function is useful for calculating totals from lists of prices,
    amounts, or other numeric values.
    
    Args:
        prices: An iterable collection of numeric values to sum
        
    Returns:
        The sum of all prices as a float
        
    Example:
        >>> prices = [9.99, 4.50, 2.00]
        >>> calculate_total(prices)
        16.49
        
        >>> calculate_total([1.5, 2.5])
        4.0
    """
    total = 0.0
    for price in prices:
        total += float(price)
    return total


def get_user_full_name(user: User) -> str:
    """Extract the full name from a User object.
    
    This is a convenience function that delegates to the User.full_name() method.
    It provides a functional interface for getting user names, which can be
    useful in contexts where you're working with function composition or
    need to pass user name extraction as a callback.
    
    Args:
        user: A User object to extract the name from
        
    Returns:
        The user's full name as a string
        
    Example:
        >>> user = User(UserId(1), "Ada", "Lovelace", "ada@example.com")
        >>> get_user_full_name(user)
        'Ada Lovelace'
    """
    return user.full_name()


def multiply_matrices(matrix1: Matrix, matrix2: Matrix) -> Matrix:
    """Multiply two matrices together.
    
    Performs standard matrix multiplication where the result is a new matrix
    with dimensions (matrix1.rows × matrix2.cols).
    
    Args:
        matrix1: First matrix (left operand)
        matrix2: Second matrix (right operand)
        
    Returns:
        A new Matrix that is the product of the two input matrices
        
    Raises:
        ValueError: If the number of columns in matrix1 doesn't match
                   the number of rows in matrix2
        
    Example:
        >>> m1 = Matrix([[1, 2], [3, 4]])
        >>> m2 = Matrix([[5, 6], [7, 8]])
        >>> result = multiply_matrices(m1, m2)
        >>> print(result)
        Matrix(2x2):
        [19, 22]
        [43, 50]
    """
    if matrix1.cols != matrix2.rows:
        raise ValueError(
            f"Cannot multiply matrices: {matrix1.rows}x{matrix1.cols} and {matrix2.rows}x{matrix2.cols}. "
            f"Number of columns in first matrix must equal number of rows in second matrix."
        )
    
    result_data = []
    for i in range(matrix1.rows):
        row = []
        for j in range(matrix2.cols):
            element = sum(matrix1.data[i][k] * matrix2.data[k][j] for k in range(matrix1.cols))
            row.append(element)
        result_data.append(row)
    
    return Matrix(result_data)


def create_identity_matrix(size: int) -> Matrix:
    """Create an identity matrix of the specified size.
    
    An identity matrix is a square matrix with 1s on the diagonal and 0s elsewhere.
    When multiplied by any matrix of compatible size, it returns the original matrix.
    
    Args:
        size: The size of the square identity matrix
        
    Returns:
        A new Matrix that is an identity matrix
        
    Raises:
        ValueError: If size is less than 1
        
    Example:
        >>> identity = create_identity_matrix(3)
        >>> print(identity)
        Matrix(3x3):
        [1, 0, 0]
        [0, 1, 0]
        [0, 0, 1]
    """
    if size < 1:
        raise ValueError("Matrix size must be at least 1")
    
    data = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(1.0 if i == j else 0.0)
        data.append(row)
    
    return Matrix(data)


def matrix_determinant(matrix: Matrix) -> float:
    """Calculate the determinant of a square matrix.
    
    Uses the Laplace expansion method for calculating determinants.
    Only works for square matrices.
    
    Args:
        matrix: The square matrix to calculate the determinant for
        
    Returns:
        The determinant of the matrix
        
    Raises:
        ValueError: If the matrix is not square
        
    Example:
        >>> matrix = Matrix([[1, 2], [3, 4]])
        >>> determinant = matrix_determinant(matrix)
        >>> print(determinant)
        -2.0
    """
    if matrix.rows != matrix.cols:
        raise ValueError("Determinant can only be calculated for square matrices")
    
    # Base case: 1x1 matrix
    if matrix.rows == 1:
        return matrix.data[0][0]
    
    # Base case: 2x2 matrix
    if matrix.rows == 2:
        return matrix.data[0][0] * matrix.data[1][1] - matrix.data[0][1] * matrix.data[1][0]
    
    # Recursive case: use Laplace expansion
    determinant = 0.0
    for col in range(matrix.cols):
        # Create submatrix by removing first row and current column
        submatrix_data = []
        for i in range(1, matrix.rows):
            row = []
            for j in range(matrix.cols):
                if j != col:
                    row.append(matrix.data[i][j])
            submatrix_data.append(row)
        
        submatrix = Matrix(submatrix_data)
        cofactor = matrix.data[0][col] * matrix_determinant(submatrix)
        
        # Alternate signs
        if col % 2 == 0:
            determinant += cofactor
        else:
            determinant -= cofactor
    
    return determinant


def matrix_trace(matrix: Matrix) -> float:
    """Calculate the trace of a square matrix.
    
    The trace is the sum of elements on the main diagonal.
    
    Args:
        matrix: The square matrix to calculate the trace for
        
    Returns:
        The trace of the matrix
        
    Raises:
        ValueError: If the matrix is not square
        
    Example:
        >>> matrix = Matrix([[1, 2], [3, 4]])
        >>> trace = matrix_trace(matrix)
        >>> print(trace)
        5.0
    """
    if matrix.rows != matrix.cols:
        raise ValueError("Trace can only be calculated for square matrices")
    
    return sum(matrix.data[i][i] for i in range(matrix.rows))
