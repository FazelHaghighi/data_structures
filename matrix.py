def determinant(matrix):
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for c in range(len(matrix)):
            det += ((-1) ** c) * matrix[0][c] * determinant(submatrix(matrix, 0, c))
        return det


def submatrix(matrix, row, col):
    submatrix = []
    for i in range(len(matrix)):
        if i != row:
            submatrix.append([])
            for j in range(len(matrix)):
                if j != col:
                    submatrix[-1].append(matrix[i][j])
    return submatrix


matrix = [[1, 4, 2], [0, 2, 6], [5, 4, 1]]
print(determinant(matrix))
