from typing import List

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    r, c, m, n = 0, 0, len(matrix), len(matrix[0])
    result = []
    tr, direction = 0, 1 # tr: 0 - row, 1 - col, direction: -1 - backward, 1 - forward
    while 0 <= r < m and 0 <= c < n and matrix[r][c] is not None:
        result.append(matrix[r][c])
        matrix[r][c] = None # visited
        if tr == 0:
            if direction == 1:
                if c < n - 1 and matrix[r][c + 1] is not None:
                    c += 1
                else:
                    tr = 1
                    r += 1
            else:
                if c > 0 and matrix[r][c - 1] is not None:
                    c -= 1
                else:
                    tr = 1
                    r -= 1
        else:
            if direction == 1:
                if r < m - 1 and matrix[r + 1][c] is not None:
                    r += 1
                else:
                    tr = 0
                    c -= 1                    
                    direction *= -1
            else:
                if r > 0 and matrix[r - 1][c] is not None:
                    r -= 1
                else:
                    tr = 0
                    c += 1
                    direction *= -1
    return result

if __name__ == "__main__":
    #matrix = [[1,2,3],[4,5,6],[7,8,9]]
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(spiralOrder(matrix))