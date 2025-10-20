"""Main entry point for the typed-python-starter application.

This module demonstrates the usage of the typed Python application by creating
a sample user, calculating totals, and demonstrating matrix operations.
"""

from __future__ import annotations

from .functions import (
    calculate_total, 
    get_user_full_name, 
    multiply_matrices, 
    create_identity_matrix,
    matrix_determinant,
    matrix_trace
)
from .models import User, UserId, Matrix


def main() -> None:
    """Main application entry point.
    
    This function demonstrates the core functionality of the application:
    - Creating a user with typed data
    - Calculating totals from a list of prices
    - Demonstrating matrix operations
    - Formatting and displaying output
    
    The function serves as both a demo and a template for how to use
    the application's modules together.
    """
    print("=== Typed Python Starter Demo ===\n")
    
    # 1. User operations
    print("1. User Operations:")
    user = User(id=UserId(1), first_name="Ada", last_name="Lovelace", email="ada@example.com")
    name = get_user_full_name(user)
    print(f"   User: {name}")
    
    # 2. Price calculations
    print("\n2. Price Calculations:")
    prices = [9.99, 4.50, 2.00]
    total = calculate_total(prices)
    print(f"   Prices: {prices}")
    print(f"   Total: {total:.2f}")
    
    # 3. Matrix operations
    print("\n3. Matrix Operations:")
    
    # Create sample matrices
    matrix_a = Matrix([[1, 2, 3], [4, 5, 6]])
    matrix_b = Matrix([[7, 8], [9, 10], [11, 12]])
    matrix_square = Matrix([[2, 1], [3, 4]])
    
    print("   Matrix A (2x3):")
    print(f"   {str(matrix_a).replace(chr(10), chr(10) + '   ')}")
    
    print("\n   Matrix B (3x2):")
    print(f"   {str(matrix_b).replace(chr(10), chr(10) + '   ')}")
    
    # Matrix multiplication
    result_matrix = multiply_matrices(matrix_a, matrix_b)
    print("\n   A × B (Matrix Multiplication):")
    print(f"   {str(result_matrix).replace(chr(10), chr(10) + '   ')}")
    
    # Matrix addition
    matrix_c = Matrix([[1, 2], [3, 4]])
    matrix_d = Matrix([[5, 6], [7, 8]])
    sum_matrix = matrix_c + matrix_d
    print("\n   Matrix C + Matrix D (Addition):")
    print(f"   {str(sum_matrix).replace(chr(10), chr(10) + '   ')}")
    
    # Scalar multiplication
    scaled_matrix = matrix_c * 2
    print("\n   Matrix C × 2 (Scalar Multiplication):")
    print(f"   {str(scaled_matrix).replace(chr(10), chr(10) + '   ')}")
    
    # Matrix transpose
    transposed = matrix_c.transpose()
    print("\n   Matrix C Transpose:")
    print(f"   {str(transposed).replace(chr(10), chr(10) + '   ')}")
    
    # Identity matrix
    identity = create_identity_matrix(3)
    print("\n   3x3 Identity Matrix:")
    print(f"   {str(identity).replace(chr(10), chr(10) + '   ')}")
    
    # Matrix determinant
    determinant = matrix_determinant(matrix_square)
    print(f"\n   Determinant of Matrix Square: {determinant}")
    
    # Matrix trace
    trace = matrix_trace(matrix_square)
    print(f"   Trace of Matrix Square: {trace}")
    
    # Final summary
    print(f"\n=== Summary ===")
    print(f"Hello, {name}! Your total is {total:.2f}.")
    print(f"Matrix operations completed successfully!")
    print(f"Matrix A×B result dimensions: {result_matrix.rows}x{result_matrix.cols}")


if __name__ == "__main__":
    main()
