'''
6. Zero Matrix
Question​: Given a boolean matrix, update it so that if any cell is true, all the cells in that
row and column are true.
eg.
[true,​ ​false​,​ ​false​]​ ​     [true,​ ​true​,​ ​true​ ​]
[false,​ ​false​,​ ​false​]​ ​->​  ​[true,​ ​false​,​ ​false​]
[false,​ ​false​,​ ​false​]​     ​[true,​ ​false​,​ ​false​]
'''
from typing import List
import unittest

# Time complexity: O(n), Space complexity: O(n)
def transform_matrix1(matrix:List[List[int]]):
    true_rows = set()
    true_cols = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]:
                true_rows.add(i)
                true_cols.add(j)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in true_rows or j in true_cols:
                matrix[i][j] = True
                
# Time complexity: O(n), Space complexity: O(1) SPACE EFFICIENT
def transform_matrix(matrix:List[List[int]]):
    firstRowTrue, firstColTrue = False, False
    for j in range(len(matrix[0])):
        firstRowTrue = firstRowTrue or matrix[0][j]
    
    for i in range(len(matrix)):
        firstColTrue = firstColTrue or matrix[i][0]

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j]:
                matrix[0][j] = True
                matrix[i][0] = True
    
    for j in range(1, len(matrix[0])):
        if matrix[0][j]:
            for i in range(len(matrix)):
                matrix[i][j] = True

    for i in range(1, len(matrix)):
        if matrix[i][0]:
            for j in range(len(matrix[0])):
                matrix[i][j] = True

    if firstRowTrue:
        for j in range(len(matrix[0])):
            matrix[0][j] = True

    if firstColTrue:
        for i in range(len(matrix)):
            matrix[i][0] = True

class Tests(unittest.TestCase):
    def test_ex1(self):
        matrix = [[True, False, False], [False, False, False], [False, False, False]]
        transform_matrix(matrix)
        expected = [[True, True, True], [True, False, False], [True, False, False]]
        self.assertEqual(expected, matrix)

    def test_ex2(self):
        matrix = [[False, False, False], [False, True, False], [False, False, False]]
        transform_matrix(matrix)
        expected = [[False, True, False], [True, True, True], [False, True, False]]
        self.assertEqual(expected, matrix)

if __name__ == "__main__":
    unittest.main(verbosity = 2)