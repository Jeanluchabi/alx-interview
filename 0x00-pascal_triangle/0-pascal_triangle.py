#!/usr/bin/python3
"""
This is a script to create a function 'pascal_triangle(n)' that
returns a list of lists representing pascal's triangle of n.
"""


def pascal_triangle(n):
    """
    This is a function to return pascal's triangle of n.
    """

    # Check if n is less than or equal to 0
    if n <= 0:
        return []

    # Initialize the triangle with the first row containing 1
    triangle = [[1]]

    # Iterate from the second row to the nth row
    for i in range(1, n):
        # Initialize the current row with 1
        row = [1]

        # Iterate from the second column to the (i-1)th column
        for j in range(1, i):
            # Calculate the value for the current cell
            # by summing the values from the previous row
            cell_value = triangle[i - 1][j - 1] + triangle[i - 1][j]
            # Append the cell value to the current row
            row.append(cell_value)

        # Append 1 to the end of the current row
        row.append(1)

        # Append the current row to the triangle
        triangle.append(row)

    # Return the pascal's triangle
    return triangle
