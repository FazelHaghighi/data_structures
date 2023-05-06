class SparseMatrix:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value
        self.matrix = self.create_matrix()
        self.row_index = self.create_index(self.matrix, True)
        self.col_index = self.create_index(self.matrix, False)

    def create_matrix(self):
        matrix = [[0] * self.col for _ in range(self.row)]
        for i, j, val in self.value:
            matrix[i][j] = val
        return matrix

    def create_index(self, matrix, is_row):
        index = [[] for _ in range(self.row if is_row else self.col)]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (is_row and matrix[i][j] != 0) or (not is_row and matrix[j][i] != 0):
                    index[i].append(j)
        return index

    def multiply(self, other):
        if self.col != other.row:
            print("Error: The two matrices cannot be multiplied.")
            return None

        result = []
        for i in range(self.row):
            for j in range(other.col):
                val = sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.col))
                if val != 0:
                    result.append([i, j, val])
        return result

    def transpose(self):
        result = []
        for i in range(self.col):
            for j in range(self.row):
                if self.matrix[j][i] != 0:
                    result.append([i, j, self.matrix[j][i]])
        return result


if __name__ == "__main__":
    m1 = SparseMatrix(
        3, 3, [[0, 0, 1], [0, 1, 2], [1, 0, 3], [1, 1, 4], [2, 0, 5], [2, 1, 6]]
    )
    m2 = SparseMatrix(
        3, 3, [[0, 0, 1], [0, 1, 2], [1, 0, 3], [1, 1, 4], [2, 0, 5], [2, 1, 6]]
    )

    print(m1.multiply(m2))
    print(m1.transpose())
