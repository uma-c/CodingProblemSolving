'''
Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
 

Example 1:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
Example 2:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-109 <= matix[i][j] <= 109
All the integers in each row are sorted in ascending order.
All the integers in each column are sorted in ascending order.
-109 <= target <= 109
'''
from typing import List

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    def _searchMatrix(matrix: List[List[int]], target: int, i: int, j: int, p: int, q: int) -> bool:
        if 0 <= i < len(matrix) and 0 <= p < len(matrix) and 0 <= j < len(matrix[0]) and 0 <= q < len(matrix[0]):
            if not (matrix[i][j] <= target <= matrix[p][q]):
                return False
            if i == p and j == q:
                return matrix[i][j] == target
            rm = i + (p - i) // 2
            cm = j + (q - j) // 2
            if matrix[rm][cm] == target:
                return True        
            return _searchMatrix(matrix, target, i, j, rm, cm) \
                or _searchMatrix(matrix, target, i, cm + 1, rm, q) \
                or _searchMatrix(matrix, target, rm + 1, j, p, cm) \
                or _searchMatrix(matrix, target, rm + 1, cm + 1, p, q)
        else:
            return False
    return _searchMatrix(matrix, target, 0, 0, len(matrix) - 1, len(matrix[0]) - 1)

if __name__ == "__main__":
    matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    print(searchMatrix(matrix, 5))
