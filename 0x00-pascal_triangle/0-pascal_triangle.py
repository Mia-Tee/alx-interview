#!/usr/bin/python3
"""
Defines a function that generates Pascal's triangle.
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal’s triangle of n.
    
    Args:
        n: number of rows for Pascal’s triangle
    
    Returns:
        A list of lists of integers representing the Pascal’s triangle.
        If n <= 0, returns an empty list.
    """
    if n <= 0:
        return []
    
    triangle = [[1]]  # First row of Pascal's triangle
    
    # Generate the rows
    for i in range(1, n):
        row = [1]  # Every row starts with 1
        for j in range(1, i):
            # Sum of the two values directly above
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # Every row ends with 1
        triangle.append(row)
    
    return triangle
