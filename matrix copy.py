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

    def print_matrix(self):
        for i in range(self.row):
            for j in range(self.col):
                print(self.matrix[i][j], end=" ")
            print()

    def print_row_index(self):
        for i in range(self.row):
            print(i, end=" ")
            for j in range(len(self.row_index[i])):
                print(self.row_index[i][j], end=" ")
            print()

    def print_col_index(self):
        for i in range(self.col):
            print(i, end=" ")
            for j in range(len(self.col_index[i])):
                print(self.col_index[i][j], end=" ")
            print()

    def get_value(self, row, col):
        return self.matrix[row][col]

    def get_row_index(self, row):
        return self.row_index[row]

    def get_col_index(self, col):
        return self.col_index[col]

    def add(self, other):
        if self.row != other.row or self.col != other.col:
            print("Error: The two matrixs are not the same size.")
            return None
        else:
            result = []
            for i in range(self.row):
                for j in range(self.col):
                    if self.matrix[i][j] + other.matrix[i][j] != 0:
                        result.append([i, j, self.matrix[i][j] + other.matrix[i][j]])

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

    def fast_transpose(self):
        result = []
        for i in range(self.col):
            for j in range(len(self.col_index[i])):
                result.append(
                    [i, self.col_index[i][j], self.matrix[self.col_index[i][j]][i]]
                )
        return result

    def multiply_fast(self, other):
        if self.col != other.row:
            print("Error: The two matrixs can not be multiplied.")
            return None
        else:
            result = []
            for i in range(self.row):
                for j in range(len(self.row_index[i])):
                    for k in range(len(other.col_index[self.row_index[i][j]])):
                        result.append(
                            [
                                i,
                                other.col_index[self.row_index[i][j]][k],
                                self.matrix[i][self.row_index[i][j]]
                                * other.matrix[self.row_index[i][j]][
                                    other.col_index[self.row_index[i][j]][k]
                                ],
                            ]
                        )
            return result


# Path: data_structure\assignment2\main.py
from matrix import sparse_matrix

if __name__ == "__main__":
    m1 = sparse_matrix(
        3, 3, [[0, 0, 1], [0, 1, 2], [1, 0, 3], [1, 1, 4], [2, 0, 5], [2, 1, 6]]
    )
    m1.print_matrix()
    m1.print_row_index()
    m1.print_col_index()
    print(m1.get_value(0, 0))
    print(m1.get_row_index(0))
    print(m1.get_col_index(0))
    m2 = sparse_matrix(
        3, 3, [[0, 0, 1], [0, 1, 2], [1, 0, 3], [1, 1, 4], [2, 0, 5], [2, 1, 6]]
    )
    print(m1.add(m2))
    print(m1.multiply(m2))
    print(m1.transpose())
    print(m1.fast_transpose())
    print(m1.multiply_fast(m2))
