def determinant(matrix):
    size = len(matrix)
    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for col in range(size):
            det += ((-1) ** col) * matrix[0][col] * determinant(get_submatrix(matrix, 0, col))
        return det


def get_submatrix(matrix, row, col):
    submatrix = []
    for i in range(len(matrix)):
        if i != row:
            subrow = []
            for j in range(len(matrix)):
                if j != col:
                    subrow.append(matrix[i][j])
            submatrix.append(subrow)
    return submatrix


matrix = [[1, 4, 2], [0, 2, 6], [5, 4, 1]]
print(determinant(matrix))
