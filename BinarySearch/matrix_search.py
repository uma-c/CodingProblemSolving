from typing import List
import unittest

def get_matrix_row_col(index:int, rows: int, cols: int)->List[int]:
    i = index // cols 
    j = index - (cols * i)
    return [i, j]

def search(matrix:List[List[int]], e: int) -> List[int]:
    rows, cols = len(matrix), len(matrix[0]) if len(matrix) > 0 else 0
    left, right = 0, (rows * cols) - 1
    while left <= right:
        m = left + ((right - left) // 2)
        i, j = get_matrix_row_col(m, rows, cols)
        if matrix[i][j] == e:
            return [i, j]
        elif matrix[i][j] > e:
            right = m - 1
        else:
            left = m + 1

    return [None, None]


def search1(matrix:List[List[int]], e: int) -> List[int]:
    rows, cols = len(matrix), len(matrix[0]) if len(matrix) > 0 else 0
    r, c = rows // 2, cols - 1
    while r < rows and c >= 0:
        if matrix[r][c] == e:
            return [r, c]
        elif matrix[r][c] < e:
            r += 1
        else:
            c -= 1

    return [None, None]

class Tests(unittest.TestCase):
    def test_ex1(self):
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        result = search(matrix, 7)
        self.assertEqual([1, 2], result)

    def test_ex2(self):
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        result = search(matrix, 15)
        self.assertEqual([None, None], result)

    def test_ex3(self):
        matrix = []
        result = search(matrix, 1)
        self.assertEqual([None, None], result)

    def test_get_matrix_row_col1(self):
        result = get_matrix_row_col(7, 3, 4)
        self.assertEqual([1, 3], result)

    def test_get_matrix_row_col2(self):
        result = get_matrix_row_col(11, 3, 4)
        self.assertEqual([2, 3], result)

if __name__ == "__main__":
    unittest.main(verbosity = 2)