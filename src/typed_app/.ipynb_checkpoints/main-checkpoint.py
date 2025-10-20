"""Main entry point for the typed-python-starter application.

This module demonstrates the usage of the typed Python application by creating
a sample user, calculating totals, and displaying formatted output.
"""

from __future__ import annotations

from .functions import calculate_total, get_user_full_name
from .models import User, UserId


def main() -> None:
    """Main application entry point.
    
    This function demonstrates the core functionality of the application:
    - Creating a user with typed data
    - Calculating totals from a list of prices
    - Formatting and displaying output
    
    The function serves as both a demo and a template for how to use
    the application's modules together.
    """
    # Create a sample user using the typed User model
    user = User(id=UserId(1), first_name="Ada", last_name="Lovelace", email="ada@example.com")
    
    # Define some sample prices to calculate
    prices = [9.99, 4.50, 2.00]
    
    # Calculate the total using our utility function
    total = calculate_total(prices)
    
    # Get the user's formatted full name
    name = get_user_full_name(user)
    
    # Display the results
    print(f"Hello, {name}! Your total is {total:.2f}.")


if __name__ == "__main__":
    main()
