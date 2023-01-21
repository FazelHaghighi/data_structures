class sparse_matrix:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value
        self.matrix = self.create_matrix()
        self.row_index = self.create_row_index()
        self.col_index = self.create_col_index()

    def create_matrix(self):
        matrix = []
        for i in range(self.row):
            matrix.append([])
            for j in range(self.col):
                matrix[i].append(0)
        for i in range(len(self.value)):
            matrix[self.value[i][0]][self.value[i][1]] = self.value[i][2]
        return matrix

    def create_row_index(self):
        row_index = []
        for i in range(self.row):
            row_index.append([])
            for j in range(self.col):
                if self.matrix[i][j] != 0:
                    row_index[i].append(j)
        return row_index

    def create_col_index(self):
        col_index = []
        for i in range(self.col):
            col_index.append([])
            for j in range(self.row):
                if self.matrix[j][i] != 0:
                    col_index[i].append(j)
        return col_index

    def multiply(self, other):
        if self.col != other.row:
            print("Error: The two matrixs can not be multiplied.")
            return None
        else:
            result = []
            for i in range(self.row):
                for j in range(other.col):
                    sum = 0
                    for k in range(self.col):
                        sum += self.matrix[i][k] * other.matrix[k][j]
                    if sum != 0:
                        result.append([i, j, sum])
            return result

    def transpose(self):
        result = []
        for i in range(self.col):
            for j in range(self.row):
                if self.matrix[j][i] != 0:
                    result.append([i, j, self.matrix[j][i]])
        return result


from sparse_matrix import sparse_matrix

if __name__ == "__main__":
    m1 = sparse_matrix(
        3, 3, [[0, 0, 1], [0, 1, 2], [1, 0, 3], [1, 1, 4], [2, 0, 5], [2, 1, 6]]
    )
    m2 = sparse_matrix(
        3, 3, [[0, 0, 1], [0, 1, 2], [1, 0, 3], [1, 1, 4], [2, 0, 5], [2, 1, 6]]
    )

    print(m1.multiply(m2))
    print(m1.transpose())
