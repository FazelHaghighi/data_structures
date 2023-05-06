class SparseMatrix:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value
        self.matrix = self._create_matrix()
        self.row_index = self._create_row_index()
        self.col_index = self._create_col_index()

    def _create_matrix(self):
        matrix = [[0] * self.col for _ in range(self.row)]
        for i, j, val in self.value:
            matrix[i][j] = val
        return matrix

    def _create_row_index(self):
        row_index = [[] for _ in range(self.row)]
        for i in range(self.row):
            row_index[i] = [j for j in range(self.col) if self.matrix[i][j] != 0]
        return row_index

    def _create_col_index(self):
        col_index = [[] for _ in range(self.col)]
        for i in range(self.col):
            col_index[i] = [j for j in range(self.row) if self.matrix[j][i] != 0]
        return col_index

    def print_matrix(self):
        for row in self.matrix:
            print(' '.join(map(str, row)))

    def print_row_index(self):
        for i, row in enumerate(self.row_index):
            print(i, ' '.join(map(str, row)))

    def print_col_index(self):
        for i, col in enumerate(self.col_index):
            print(i, ' '.join(map(str, col)))

    def get_value(self, row, col):
        return self.matrix[row][col]

    def get_row_index(self, row):
        return self.row_index[row]

    def get_col_index(self, col):
        return self.col_index[col]

    def add(self, other):
        if self.row != other.row or self.col != other.col:
            print("Error: The two matrices are not the same size.")
            return None
        else:
            result = SparseMatrix(self.row, self.col, [])
            result.value = [[i, j, self.matrix[i][j] + other.matrix[i][j]] for i in range(self.row) for j in range(self.col) if self.matrix[i][j] + other.matrix[i][j] != 0]
            result.matrix = result._create_matrix()
            result.row_index = result._create_row_index()
            result.col_index = result._create_col_index()
            return result

    def multiply(self, other):
        if self.col != other.row:
            print("Error: The two matrices cannot be multiplied.")
            return None
        else:
            result = SparseMatrix(self.row, other.col, [])
            for i in range(self.row):
                for j in range(other.col):
                    val = sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.col))
                    if val != 0:
                        result.value.append([i, j, val])
            result.matrix = result._create_matrix()
            result.row_index = result._create_row_index()
            result.col_index = result._create_col_index()
            return result

    def transpose(self):
        result = SparseMatrix(self.col, self.row, [])
        for i in range(self.col):
            for j in range(self.row):
                if self.matrix[j][i] != 0:
                    result.value.append([i, j, self.matrix[j][i]])
        result.matrix = result._create_matrix()
        result.row_index = result._create_row_index()
        result.col_index = result._create_col_index()
        return result

    def fast_transpose(self):
        result = SparseMatrix(self.col,
        self.row, self.value)
        for i in range(self.col):
            for j in range(len(self.col_index[i])):
                result.value.append([i, self.col_index[i][j], self.matrix[self.col_index[i][j]][i]])
        result.matrix = result._create_matrix()
        result.row_index = result._create_row_index()
        result.col_index = result._create_col_index()
        return result
    
    def multiply_fast(self, other):
        if self.col != other.row:
            print("Error: The two matrices cannot be multiplied.")
            return None
        else:
            result = SparseMatrix(self.row, other.col, [])
            for i in range(self.row):
                for j in range(len(self.row_index[i])):
                    for k in range(len(other.col_index[self.row_index[i][j]])):
                        val = (
                            self.matrix[i][self.row_index[i][j]]
                            * other.matrix[self.row_index[i][j]][other.col_index[self.row_index[i][j]][k]]
                        )
                        if val != 0:
                            result.value.append([i, other.col_index[self.row_index[i][j]][k], val])
            result.matrix = result._create_matrix()
            result.row_index = result._create_row_index()
            result.col_index = result._create_col_index()
            return result



# Path: data_structure\assignment2\main.py
if __name__ == "__main__":
    m1 = SparseMatrix(3, 3, [[0, 0, 1], [0, 1, 2], [1, 0, 3], [1, 1, 4], [2, 0, 5], [2, 1, 6]])
    m1.print_matrix()
    m1.print_row_index()
    m1.print_col_index()
    print(m1.get_value(0, 0))
    print(m1.get_row_index(0))
    print(m1.get_col_index(0))
    m2 = SparseMatrix(3, 3, [[0, 0, 1], [0, 1, 2], [1, 0, 3], [1, 1, 4], [2, 0, 5], [2, 1, 6]])
    print(m1.add(m2))
    print(m1.multiply(m2))
    print(m1.transpose())
    print(m1.fast_transpose())
    print(m1.multiply_fast(m2))
