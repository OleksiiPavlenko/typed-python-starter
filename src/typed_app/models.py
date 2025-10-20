"""User data models and mathematical structures for the typed-python-starter application.

This module defines the core data structures used throughout the application,
including user identification, user information models, and mathematical structures like matrices.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import NewType

UserId = NewType("UserId", int)


@dataclass(frozen=True, slots=True)
class User:
    """Represents a user in the system.
    
    This is an immutable dataclass that stores user information.
    The frozen=True ensures immutability, and slots=True optimizes memory usage.
    
    Attributes:
        id: Unique identifier for the user
        first_name: User's first name
        last_name: User's last name  
        email: User's email address
        
    Example:
        >>> user = User(
        ...     id=UserId(1),
        ...     first_name="Ada",
        ...     last_name="Lovelace", 
        ...     email="ada@example.com"
        ... )
        >>> user.full_name()
        'Ada Lovelace'
    """
    
    id: UserId
    first_name: str
    last_name: str
    email: str

    def full_name(self) -> str:
        """Get the user's full name.
        
        Combines the first and last name into a single string.
        Handles cases where names might have extra whitespace.
        
        Returns:
            The user's full name with any trailing/leading whitespace removed.
            
        Example:
            >>> user = User(UserId(1), "Ada", "Lovelace", "ada@example.com")
            >>> user.full_name()
            'Ada Lovelace'
        """
        return f"{self.first_name} {self.last_name}".strip()


@dataclass(frozen=True, slots=True)
class Matrix:
    """Represents a mathematical matrix.
    
    This is an immutable dataclass that stores matrix data as a list of lists.
    The matrix supports basic mathematical operations like addition, multiplication,
    and scalar operations.
    
    Attributes:
        data: 2D list representing the matrix elements
        rows: Number of rows in the matrix
        cols: Number of columns in the matrix
        
    Example:
        >>> matrix = Matrix([[1, 2], [3, 4]])
        >>> print(matrix)
        Matrix(2x2):
        [1, 2]
        [3, 4]
    """
    
    data: list[list[float]]
    
    def __post_init__(self) -> None:
        """Validate matrix data after initialization."""
        if not self.data:
            raise ValueError("Matrix cannot be empty")
        
        # Check if all rows have the same length
        first_row_length = len(self.data[0])
        for row in self.data:
            if len(row) != first_row_length:
                raise ValueError("All rows must have the same length")
    
    @property
    def rows(self) -> int:
        """Get the number of rows in the matrix."""
        return len(self.data)
    
    @property
    def cols(self) -> int:
        """Get the number of columns in the matrix."""
        return len(self.data[0]) if self.data else 0
    
    def __str__(self) -> str:
        """String representation of the matrix."""
        lines = [f"Matrix({self.rows}x{self.cols}):"]
        for row in self.data:
            lines.append(str(row))
        return "\n".join(lines)
    
    def __repr__(self) -> str:
        """Detailed representation of the matrix."""
        return f"Matrix({self.data})"
    
    def get_element(self, row: int, col: int) -> float:
        """Get element at specified position.
        
        Args:
            row: Row index (0-based)
            col: Column index (0-based)
            
        Returns:
            The element at the specified position
            
        Raises:
            IndexError: If row or col is out of bounds
        """
        if not (0 <= row < self.rows):
            raise IndexError(f"Row index {row} out of bounds (0-{self.rows-1})")
        if not (0 <= col < self.cols):
            raise IndexError(f"Column index {col} out of bounds (0-{self.cols-1})")
        return self.data[row][col]
    
    def transpose(self) -> Matrix:
        """Return the transpose of the matrix.
        
        Returns:
            A new Matrix object that is the transpose of this matrix
        """
        transposed_data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return Matrix(transposed_data)
    
    def __add__(self, other: Matrix) -> Matrix:
        """Add two matrices element-wise.
        
        Args:
            other: Another matrix to add
            
        Returns:
            A new Matrix that is the sum of the two matrices
            
        Raises:
            ValueError: If matrices have different dimensions
        """
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError(f"Cannot add matrices of different sizes: {self.rows}x{self.cols} and {other.rows}x{other.cols}")
        
        result_data = [
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result_data)
    
    def __mul__(self, scalar: float) -> Matrix:
        """Multiply matrix by a scalar.
        
        Args:
            scalar: The scalar value to multiply by
            
        Returns:
            A new Matrix with all elements multiplied by the scalar
        """
        result_data = [
            [self.data[i][j] * scalar for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result_data)
    
    def __rmul__(self, scalar: float) -> Matrix:
        """Right multiplication by scalar (scalar * matrix)."""
        return self * scalar
