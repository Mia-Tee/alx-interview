#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []
    
    # Initialize the triangle with the first row
    triangle = [[1]]

    # Generate the next rows of the triangle
    for i in range(1, n):
        row = [1]  # Each row starts with 1
        for j in range(1, i):
            # Compute the value based on the sum of two values from the previous row
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # Each row ends with 1
        triangle.append(row)

    return triangle
