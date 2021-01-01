import unittest
from typing import List

# top down
def max_square_submatrix_dp(matrix: List[List[bool]], cache: List[List[int]], i: int, j: int) -> int:
    m = len(matrix) # rows
    n = len(matrix[0]) if m > 0 else 0 # columns    
    if not (i < m and j < n):
        return 0
    if not cache[i][j] < 0:
        return cache[i][j]

    if matrix[i][j]:
        i_1_j = max_square_submatrix_dp(matrix, cache, i + 1, j)
        i_j_1 = max_square_submatrix_dp(matrix, cache, i, j + 1)
        i_1_j_1 = max_square_submatrix_dp(matrix, cache, i + 1, j + 1)
        return 1 + min(i_1_j, i_j_1, i_1_j_1)
    else:
        return 0

def max_square_submatrix(matrix: List[List[bool]]) -> int:
    m = len(matrix) # rows
    n = len(matrix[0]) if m > 0 else 0 # columns
    cache = [[-1 for _ in range(n)] for _ in range(m)]
    ans = float("-inf")
    for i in range(m):        
        for j in range(n):
            ans = max(max_square_submatrix_dp(matrix, cache, i, j), ans)
    return ans

#bottom up dp
def max_square_submatrix1(matrix: List[List[bool]]) -> int:
    m = len(matrix) # rows
    n = len(matrix[0]) if m > 0 else 0 # columns
    if not (m > 0 and n > 0):
        return 0
    cache = [[0 for _ in range(n)] for _ in range(m)]
    ans = cache[0][0] = 1 if matrix[0][0] else 0
    for i in range(m):        
        for j in range(n):
            if matrix[i][j]:
                cache[i][j] = min(cache[i][j - 1], cache[i-1][j], cache[i-1][j-1]) + 1
                if cache[i][j] > ans:
                    ans = cache[i][j]
    return ans

class Tests(unittest.TestCase):
    def test_ex1(self):
        matrix = [[False]]
        result = max_square_submatrix1(matrix)
        self.assertEqual(0, result)

    def test_ex2(self):
        matrix = [[False, True, False, False], [True, True, True, True], [False, True, True, False]]
        result = max_square_submatrix1(matrix)
        self.assertEqual(2, result)

    def test_ex3(self):
        matrix = [[True, True, True, True, True], [True, True, True, True, False], [True, True, True, True, False], [False, True, True, True, False], [True, False, False, False, False]]
        result = max_square_submatrix1(matrix)
        self.assertEqual(3, result)

    def test_ex4(self):
        matrix = [[True, True, True, True, True], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, False, False, False, False]]
        result = max_square_submatrix1(matrix)
        self.assertEqual(4, result)

if __name__ == "__main__":
    unittest.main(verbosity=2)