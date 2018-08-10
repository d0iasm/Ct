import unittest


def rotate_matrix(matrix):
    assert len(matrix) == len(matrix[0]), 'Incorrect Input'
    
    n = len(matrix)
    for layer in range(n//2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i] 
            matrix[first][i] = matrix[last - offset][first] # left -> top
            matrix[last - offset][first] = matrix[last][last - offset] # bottom -> left
            matrix[last][last - offset] = matrix[i][last] # right -> bottm 
            matrix[i][last] = top

    return matrix


class Test(unittest.TestCase):
    dataT = [
        ([[1,1,1],
         [2,2,2],
         [3,3,3]]
         ,
         [[3,2,1],
         [3,2,1],
         [3,2,1]])
        ,
        ([[1,2,3],
         [4,5,6],
         [7,8,9]]
         ,
         [[7,4,1],
         [8,5,2],
         [9,6,3]])
        ,
        ([[1,1,1,1],
         [2,2,2,2],
         [3,3,3,3],
         [4,4,4,4]]
         ,
         [[4,3,2,1],
          [4,3,2,1],
          [4,3,2,1],
          [4,3,2,1]]
         )
        ,
        ([[1,2,3,4,5],
          [6,7,8,9,10],
          [11,12,13,14,15],
          [16,17,18,19,20],
          [21,22,23,24,25]]
         ,
         [[21,16,11,6,1],
          [22,17,12,7,2],
          [23,18,13,8,3],
          [24,19,14,9,4],
          [25,20,15,10,5]]
         )
    ]

    dataF = [
        ([[1,1,1],
          [2,2,2],
          [3,3,3]],
         [[1,1,1],
          [2,2,2],
          [3,3,3]],
         )
    ]

    def test_true(self):
        for d in self.dataT:
            self.assertEqual(d[1], rotate_matrix(d[0]))

    def test_false(self):
        for d in self.dataF:
            self.assertNotEqual(d[1], rotate_matrix(d[0]))


if __name__ == '__main__':
    unittest.main()
