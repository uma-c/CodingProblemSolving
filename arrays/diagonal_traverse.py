from typing import List

def findDiagonalOrder(matrix: List[List[int]]) -> List[int]:
    result = []
    m, n = len(matrix), len(matrix[0])
    def up(i, j):
        if 0 <= i < m and 0 <= j < n:
            result.append(matrix[i][j])
            if i > 0 and j < n - 1:
                up(i - 1, j + 1)
            else:
                if j < n - 1:
                    down(i, j + 1)
                else:
                    down(i + 1, j)
    def down(i, j):
        if 0 <= i < m and 0 <= j < n:
            result.append(matrix[i][j])
            if i < m - 1 and j > 0:
                down(i + 1, j - 1)
            else:
                if i < m - 1:
                    up(i + 1, j)
                else:
                    up(i, j + 1)
    up(0, 0)
    return result

if __name__ == "__main__":
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    print(findDiagonalOrder(mat))