'''
3. Matrix product
Question​: Given a matrix, find the path from top left to bottom right with the greatest
product by moving only down and right.

[​1​, ​2​, ​3​]
[​4​, ​5​, ​6​]
[​7​, ​8​, ​9​]

1​ -> ​4​ -> ​7​ -> ​8​ -> ​9
2016

[​-1​, ​2​, ​3​]
[​4​, ​5​, ​-6​]
[​7​, ​8​, ​9​]

-1​ -> ​4​ -> ​5​ -> ​-6​ -> ​9
1080
'''
from typing import List, Tuple
import unittest

def _max_product(matrix: List[List[int]], i:int, j:int) -> Tuple[int]:
    if i == len(matrix) or j == len(matrix[0]):
        return (1, 1)

    product_i_1_j = _max_product(matrix, i + 1, j)
    product_i_j_1 = _max_product(matrix, i, j + 1)
    return (min(matrix[i][j] * product_i_1_j[0], matrix[i][j] * product_i_1_j[1], matrix[i][j] * product_i_j_1[0], matrix[i][j] * product_i_j_1[1]),
    max(matrix[i][j] * product_i_1_j[0], matrix[i][j] * product_i_1_j[1], matrix[i][j] * product_i_j_1[0], matrix[i][j] * product_i_j_1[1]))

def max_product(matrix: List[List[int]]) -> int:
    return _max_product(matrix, 0, 0)[1]

def _max_product_dp_top_down(matrix: List[List[int]], i:int, j:int, cache: List[List[Tuple[int]]]) -> Tuple[int]:
    if i == len(matrix) or j == len(matrix[0]):
        return (1, 1)

    if len(cache[i][j]) == 0:
        product_i_1_j = _max_product_dp_top_down(matrix, i + 1, j, cache)
        product_i_j_1 = _max_product_dp_top_down(matrix, i, j + 1, cache)
        cache[i][j] = (min(matrix[i][j] * product_i_1_j[0], matrix[i][j] * product_i_1_j[1], matrix[i][j] * product_i_j_1[0], matrix[i][j] * product_i_j_1[1]),
        max(matrix[i][j] * product_i_1_j[0], matrix[i][j] * product_i_1_j[1], matrix[i][j] * product_i_j_1[0], matrix[i][j] * product_i_j_1[1]))
    return cache[i][j]

def max_product_dp_top_down(matrix: List[List[int]]) -> int:
    cache = [[() for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    return _max_product_dp_top_down(matrix, 0, 0, cache)[1]

# Time complexity: O(rows * cols) Space compelxity: O(cols)
def max_product_dp_bottom_up(matrix: List[List[int]]) -> int:
    if matrix is None or len(matrix) < 1:
        raise ValueError("invalid input")

    prev = [None for _ in range(len(matrix[0]))]
    prev[0] = [matrix[0][0], matrix[0][0]]
    for j in range(1, len(matrix[0])):
        from_left_1 = matrix[0][j] * prev[j - 1][0]
        from_left_2 = matrix[0][j] * prev[j - 1][1]
        prev[j] = [min(from_left_1, from_left_2), max(from_left_1, from_left_2)]
    for i in range(1, len(matrix)):
        curr = [None for _ in range(len(matrix[0]))]
        from_top_1 = matrix[i][0] * prev[0][0]
        from_top_2 = matrix[i][0] * prev[0][1]
        curr[0] = [min(from_top_1, from_top_2), max(from_top_1, from_top_2)]            
        for j in range(1, len(matrix[0])):            
            from_top_1 = matrix[i][j] * prev[j][0]
            from_top_2 = matrix[i][j] * prev[j][1]
            from_left_1 = matrix[i][j] * curr[j - 1][0]
            from_left_2 = matrix[i][j] * curr[j - 1][1]
            curr[j] = [min(from_top_1, from_top_2, from_left_1, from_left_2), max(from_top_1, from_top_2, from_left_1, from_left_2)]
        prev = curr

    return prev[-1][1]
    

class Tests(unittest.TestCase):
    def test_ex1(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        product = max_product_dp_bottom_up(matrix)
        self.assertEqual(2016, product)

    def test_ex2(self):
        matrix = [[-1, 2, 3], [4, 5, -6], [7, 8, 9]]
        product = max_product_dp_bottom_up(matrix)
        self.assertEqual(1080, product)

    def test_ex3(self):
        matrix = [[1, 2], [3, 4]]
        product = max_product_dp_bottom_up(matrix)
        self.assertEqual(12, product)

    def test_ex4(self):
        matrix = None
        with self.assertRaises(ValueError):
            max_product_dp_bottom_up(matrix)

    def test_ex5(self):
        matrix = []
        with self.assertRaises(ValueError):
            max_product_dp_bottom_up(matrix)

if __name__ == "__main__":
    unittest.main(verbosity = 2)