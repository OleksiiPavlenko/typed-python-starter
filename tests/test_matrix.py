"""Tests for matrix operations and Matrix class.

This module contains comprehensive tests for the Matrix class and matrix-related
functions to ensure they work correctly and handle edge cases properly.
"""

import pytest
from src.typed_app.models import Matrix
from src.typed_app.functions import (
    multiply_matrices,
    create_identity_matrix,
    matrix_determinant,
    matrix_trace
)


class TestMatrix:
    """Test cases for the Matrix class."""
    
    def test_matrix_creation(self):
        """Test basic matrix creation."""
        data = [[1, 2], [3, 4]]
        matrix = Matrix(data)
        assert matrix.data == data
        assert matrix.rows == 2
        assert matrix.cols == 2
    
    def test_matrix_creation_empty(self):
        """Test that empty matrix creation raises ValueError."""
        with pytest.raises(ValueError, match="Matrix cannot be empty"):
            Matrix([])
    
    def test_matrix_creation_inconsistent_rows(self):
        """Test that inconsistent row lengths raise ValueError."""
        with pytest.raises(ValueError, match="All rows must have the same length"):
            Matrix([[1, 2], [3]])
    
    def test_get_element(self):
        """Test getting elements from matrix."""
        matrix = Matrix([[1, 2, 3], [4, 5, 6]])
        assert matrix.get_element(0, 0) == 1
        assert matrix.get_element(1, 2) == 6
    
    def test_get_element_out_of_bounds(self):
        """Test that getting elements out of bounds raises IndexError."""
        matrix = Matrix([[1, 2], [3, 4]])
        
        with pytest.raises(IndexError, match="Row index 2 out of bounds"):
            matrix.get_element(2, 0)
        
        with pytest.raises(IndexError, match="Column index 2 out of bounds"):
            matrix.get_element(0, 2)
    
    def test_transpose(self):
        """Test matrix transpose operation."""
        matrix = Matrix([[1, 2, 3], [4, 5, 6]])
        transposed = matrix.transpose()
        
        expected = Matrix([[1, 4], [2, 5], [3, 6]])
        assert transposed.data == expected.data
        assert transposed.rows == 3
        assert transposed.cols == 2
    
    def test_matrix_addition(self):
        """Test matrix addition."""
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[5, 6], [7, 8]])
        result = matrix1 + matrix2
        
        expected = Matrix([[6, 8], [10, 12]])
        assert result.data == expected.data
    
    def test_matrix_addition_different_sizes(self):
        """Test that adding matrices of different sizes raises ValueError."""
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[1, 2, 3], [4, 5, 6]])
        
        with pytest.raises(ValueError, match="Cannot add matrices of different sizes"):
            matrix1 + matrix2
    
    def test_scalar_multiplication(self):
        """Test scalar multiplication."""
        matrix = Matrix([[1, 2], [3, 4]])
        result = matrix * 2
        
        expected = Matrix([[2, 4], [6, 8]])
        assert result.data == expected.data
    
    def test_right_scalar_multiplication(self):
        """Test right scalar multiplication (scalar * matrix)."""
        matrix = Matrix([[1, 2], [3, 4]])
        result = 3 * matrix
        
        expected = Matrix([[3, 6], [9, 12]])
        assert result.data == expected.data
    
    def test_string_representation(self):
        """Test matrix string representation."""
        matrix = Matrix([[1, 2], [3, 4]])
        str_repr = str(matrix)
        
        expected = "Matrix(2x2):\n[1, 2]\n[3, 4]"
        assert str_repr == expected
    
    def test_repr_representation(self):
        """Test matrix repr representation."""
        matrix = Matrix([[1, 2], [3, 4]])
        repr_str = repr(matrix)
        
        expected = "Matrix([[1, 2], [3, 4]])"
        assert repr_str == expected


class TestMatrixFunctions:
    """Test cases for matrix utility functions."""
    
    def test_multiply_matrices(self):
        """Test matrix multiplication function."""
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[5, 6], [7, 8]])
        result = multiply_matrices(matrix1, matrix2)
        
        expected = Matrix([[19, 22], [43, 50]])
        assert result.data == expected.data
    
    def test_multiply_matrices_incompatible_sizes(self):
        """Test matrix multiplication with incompatible sizes."""
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        
        with pytest.raises(ValueError, match="Cannot multiply matrices"):
            multiply_matrices(matrix1, matrix2)
    
    def test_create_identity_matrix(self):
        """Test identity matrix creation."""
        identity = create_identity_matrix(3)
        
        expected = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        assert identity.data == expected.data
    
    def test_create_identity_matrix_size_zero(self):
        """Test that creating identity matrix with size 0 raises ValueError."""
        with pytest.raises(ValueError, match="Matrix size must be at least 1"):
            create_identity_matrix(0)
    
    def test_create_identity_matrix_size_negative(self):
        """Test that creating identity matrix with negative size raises ValueError."""
        with pytest.raises(ValueError, match="Matrix size must be at least 1"):
            create_identity_matrix(-1)
    
    def test_matrix_determinant_1x1(self):
        """Test determinant calculation for 1x1 matrix."""
        matrix = Matrix([[5]])
        det = matrix_determinant(matrix)
        assert det == 5.0
    
    def test_matrix_determinant_2x2(self):
        """Test determinant calculation for 2x2 matrix."""
        matrix = Matrix([[1, 2], [3, 4]])
        det = matrix_determinant(matrix)
        assert det == -2.0
    
    def test_matrix_determinant_3x3(self):
        """Test determinant calculation for 3x3 matrix."""
        matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        det = matrix_determinant(matrix)
        assert det == 0.0  # This matrix has determinant 0
    
    def test_matrix_determinant_non_square(self):
        """Test that determinant calculation for non-square matrix raises ValueError."""
        matrix = Matrix([[1, 2, 3], [4, 5, 6]])
        
        with pytest.raises(ValueError, match="Determinant can only be calculated for square matrices"):
            matrix_determinant(matrix)
    
    def test_matrix_trace(self):
        """Test trace calculation."""
        matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        trace = matrix_trace(matrix)
        assert trace == 15.0  # 1 + 5 + 9
    
    def test_matrix_trace_non_square(self):
        """Test that trace calculation for non-square matrix raises ValueError."""
        matrix = Matrix([[1, 2, 3], [4, 5, 6]])
        
        with pytest.raises(ValueError, match="Trace can only be calculated for square matrices"):
            matrix_trace(matrix)


class TestMatrixIntegration:
    """Integration tests for matrix operations."""
    
    def test_matrix_operations_chain(self):
        """Test chaining multiple matrix operations."""
        # Create matrices
        a = Matrix([[1, 2], [3, 4]])
        b = Matrix([[2, 0], [1, 3]])
        identity = create_identity_matrix(2)
        
        # Test: A + B, then multiply by 2, then add identity
        result = (a + b) * 2 + identity
        
        expected = Matrix([[7, 10], [13, 19]])  # (A+B)*2 + I
        assert result.data == expected.data
    
    def test_determinant_and_trace_relationship(self):
        """Test that determinant and trace work correctly together."""
        # For a 2x2 matrix [[a, b], [c, d]]:
        # determinant = ad - bc
        # trace = a + d
        
        matrix = Matrix([[3, 1], [2, 4]])
        det = matrix_determinant(matrix)
        trace = matrix_trace(matrix)
        
        # det = 3*4 - 1*2 = 12 - 2 = 10
        # trace = 3 + 4 = 7
        assert det == 10.0
        assert trace == 7.0
    
    def test_transpose_properties(self):
        """Test transpose properties."""
        matrix = Matrix([[1, 2, 3], [4, 5, 6]])
        transposed = matrix.transpose()
        double_transposed = transposed.transpose()
        
        # Double transpose should return original matrix
        assert double_transposed.data == matrix.data
        
        # Dimensions should be swapped
        assert transposed.rows == matrix.cols
        assert transposed.cols == matrix.rows


