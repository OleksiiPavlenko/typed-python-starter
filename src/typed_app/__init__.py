"""Typed Python Starter Application.

A modern Python project scaffold with type annotations, mypy type checking,
and comprehensive matrix operations.
"""

from .main import main
from .models import User, UserId, Matrix
from .functions import (
    calculate_total,
    get_user_full_name,
    multiply_matrices,
    create_identity_matrix,
    matrix_determinant,
    matrix_trace
)

__version__ = "0.1.0"

__all__ = [
    "main",
    "User",
    "UserId", 
    "Matrix",
    "calculate_total",
    "get_user_full_name",
    "multiply_matrices",
    "create_identity_matrix",
    "matrix_determinant",
    "matrix_trace"
]
