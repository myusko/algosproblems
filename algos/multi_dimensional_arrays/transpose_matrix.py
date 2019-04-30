def transpose_matrix(matrix):
    rows = len(matrix)
    for i in range(rows):
        for j in range(i + 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    return matrix
