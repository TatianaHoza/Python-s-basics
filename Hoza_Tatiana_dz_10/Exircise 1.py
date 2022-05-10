class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        s = ''
        for i in range(len(self.matrix)):
            s = s + '\t'.join(map(str, self.matrix[i])) + '\n'
        return s

    def __add__(self, other):
        result = []

        for i in range(len(self.matrix)):
            result.append([])
            for n in range(len(self.matrix[i])):
                result[i].append(self.matrix[i][n] + other.matrix[i][n])

        return Matrix(result)

matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[7, 8], [9, 10], [11, 12]])
print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)