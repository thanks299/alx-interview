#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        # Start each row with a list of 1's
        row = [1] * (i + 1)
        
        # Update the values in the row based on the previous row
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        
        # Append the row to the triangle
        triangle.append(row)
    
    return triangle

