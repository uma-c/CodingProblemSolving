'''
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
 

Note:

The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
'''
from typing import List
import collections

def min_d_to_zero(matrix: List[List[int]], ri: int, ci: int) -> int:
    visited_matrix = [[0] * len(row) for row in matrix]
    m, n = len(matrix), len(matrix[0])
    q = collections.deque([[ri, ci, 0]])
    visited_matrix[ri][ci] = 1
    while len(q) > 0:
        rj, cj, d = q.popleft()
        neighbors = [[rj - 1, cj], [rj + 1, cj], [rj, cj - 1], [rj, cj + 1]]
        d += 1
        for nb in neighbors:
            if 0 <= nb[0] < m and 0 <= nb[1] < n and not visited_matrix[nb[0]][nb[1]]:
                if matrix[nb[0]][nb[1]]:
                    visited_matrix[nb[0]][nb[1]] = 1
                    q.append([nb[0], nb[1], d])
                else:    
                    return d

def updateMatrix(matrix: List[List[int]]) -> List[List[int]]:
    if not matrix:
        return matrix
    m, n = len(matrix), len(matrix[0])
    d_matrix = [[float("inf")] * len(row) for row in matrix]
    q = collections.deque()
    for ri in range(len(matrix)):
        for ci in range(len(matrix[0])):
            if not matrix[ri][ci]:
                q.append([ri, ci])
                d_matrix[ri][ci] = 0
    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    while len(q) > 0:
        rj, cj = q.popleft()
        for dir in dirs:
            rn, cn = rj + dir[0], cj + dir[1]
            if 0 <= rn < m and 0 <= cn < n:
                if d_matrix[rn][cn] > d_matrix[rj][cj] + 1:
                    d_matrix[rn][cn] = d_matrix[rj][cj] + 1
                    q.append([rn, cn])
    return d_matrix

if __name__ == "__main__":
    #matrix = [[0,0,0], [0,1,0], [0,0,0]]
    matrix = [[0,0,0], [0,1,0], [1,1,1]]
    print(updateMatrix(matrix))