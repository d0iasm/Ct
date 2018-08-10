import unittest


def nullifyRow(matrix, row):
    for j in range(len(matrix[0])):
        matrix[row][j] = 0
    return matrix


def nullifyColumn(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0
    return matrix


def zero_matrix_using_array(matrix):
    h = len(matrix)
    w = len(matrix[0])

    column = [False for _ in range(h)]
    row = [False for _ in range(w)]

    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 0:
                row[i] = True
                column[j] = True

    for i in range(h):
        if row[i]:
            matrix = nullifyRow(matrix, i)

    for j in range(w):
        if column[j]:
            matrix = nullifyColumn(matrix, j)

    return matrix


def zero_matrix(matrix):
    h = len(matrix)
    w = len(matrix[0])

    row_has_zero = False
    column_has_zero = False

    for i in range(h):
        if matrix[i][0] == 0:
            column_has_zero = True
            break

    for j in range(w):
        if matrix[0][j] == 0:
            row_has_zero = True
            break

    for i in range(1, h):
        for j in range(1, w):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, h): # NOTE: start from 1
        if matrix[i][0] == 0:
            for j in range(1, w):
                matrix[i][j] = 0

    for j in range(1, w): # NOTE: start from 1
        if matrix[0][j] == 0:
            for i in range(1, h):
                matrix[i][j] = 0

    if row_has_zero:
        for j in range(w):
            matrix[0][j] = 0

    if column_has_zero:
        for i in range(h):
            matrix[i][0] = 0
            
    return matrix


class Test(unittest.TestCase):
    dataT = [
        ([[0,1,0],
         [2,2,2],
         [3,3,3]]
         ,
         [[0,0,0],
         [0,2,0],
         [0,3,0]])
        ,
        ([[1,1,0],
         [2,2,2],
         [0,3,3]]
         ,
         [[0,0,0],
         [0,2,0],
         [0,0,0]])
        ,
        ([[1,1,1],
         [2,2,2],
         [3,3,3]]
         ,
         [[1,1,1],
         [2,2,2],
         [3,3,3]])
        ,
        ([[1,1,1],
         [2,0,2],
         [3,3,3]]
         ,
         [[1,0,1],
         [0,0,0],
         [3,0,3]])
    ]

    dataF = [
        ([[1,1,1],
          [2,0,2],
          [3,3,3]],
         [[0,0,0],
          [0,0,0],
          [0,0,0]],
         )
    ]

    def test_true(self):
        for d in self.dataT:
            self.assertEqual(d[1], zero_matrix(d[0]))

    def test_false(self):
        for d in self.dataF:
            self.assertNotEqual(d[1], zero_matrix(d[0]))


if __name__ == '__main__':
    unittest.main()
