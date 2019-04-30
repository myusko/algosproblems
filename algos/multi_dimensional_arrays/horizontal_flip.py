# You are given an m x n 2D image matrix (List of Lists) where each integer represents a pixel.
# Flip it in-place along its horizontal axis.


def flip_horizontal_axis(matrix):
    rows = len(matrix)
    for row in range(rows // 2):
        matrix[row], matrix[rows - 1 - row] = matrix[rows - 1 - row], matrix[row]
    return matrix
