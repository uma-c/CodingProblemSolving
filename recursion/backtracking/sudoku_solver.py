'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

 

Example 1:


Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:


 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
'''
from typing import List

def solveSudoku(board: List[List[str]]) -> None:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    grids = [set() for _ in range(9)]
    
    def init_lookups():
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    grids[get_grid_num(r, c)].add(board[r][c])

    def isValid(row: int, col: int, val: str) -> bool:
        if val in rows[row]:
            return False
        
        if val in cols[col]:
            return False

        grid_num = get_grid_num(row, col)
        if val in grids[grid_num]:
            return False

        return True

    def get_grid_num(row: int, col: int) -> int:
        return (row // 3) * 3 + (col // 3)

    def place_value(r, c, val):
        board[r][c] = val
        rows[r].add(val)
        cols[c].add(val)
        grids[get_grid_num(r, c)].add(val)

    def remove_value(r, c):        
        rows[r].remove(board[r][c])
        cols[c].remove(board[r][c])
        grids[get_grid_num(r, c)].remove(board[r][c])
        board[r][c] = "."

    def backtrack(row, col) -> bool:
        if 0 <= row < 9 and 0 <= col < 9:
            if board[row][col] == ".":
                for i in range(1, 10):
                    val = str(i)
                    if isValid(row, col, val):
                        place_value(row, col, val)
                        if backtrack(row, col + 1):
                            return True
                        remove_value(row, col)
            else:
                return backtrack(row, col + 1)
        elif col == 9:
            return backtrack(row + 1, 0)
        else:
            return True # final solution
    
    init_lookups()
    backtrack(0, 0)

if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    solveSudoku(board)
    print(board)