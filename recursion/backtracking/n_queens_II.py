'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

 

Example 1:


Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 9
'''

def totalNQueens(n: int) -> int:
    board = [[False] * n for _ in range(n)]
    def place_queen(row: int, col: int):
        board[row][col] = True
    def remove_queen(row: int, col: int):
        board[row][col] = False
    def is_under_attack(row: int, col: int) -> bool:
        # along col up
        r = row - 1
        while r >= 0:
            if board[r][col]:
                return True
            r -= 1
        
        # along dialgonal up-left
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if board[r][c]:
                return True
            r -= 1
            c -= 1

        # along diagonal up-right
        r, c = row - 1, col + 1
        while r >= 0 and c < n:
            if board[r][c]:
                return True
            r -= 1
            c += 1

        # along dialgonal left-down
        r, c = row + 1, col - 1
        while r < n and c >= 0:
            if board[r][c]:
                return True
            r += 1
            c -= 1

        # along dialgonal right-down
        r, c = row + 1, col + 1
        while r < n and c < n:
            if board[r][c]:
                return True
            r += 1
            c += 1
        
        # along row left
        c = col - 1
        while c >= 0:
            if board[row][c]:
                return True
            c -= 1

        # along row right
        c = col + 1
        while c < n:
            if board[row][c]:
                return True
            c += 1

        # along col down
        r = row + 1
        while r < n:
            if board[r][col]:
                return True
            r += 1

        return False

    def backtrack(row: int, count:int) -> int:
        for col in range(n):
            if not is_under_attack(row, col):
                place_queen(row, col)
                if row == n - 1:
                    count += 1
                else:
                    count = backtrack(row + 1, count)
                remove_queen(row, col)
        return count
    return backtrack(0, 0)

if __name__ == "__main__":
    print(totalNQueens(4))