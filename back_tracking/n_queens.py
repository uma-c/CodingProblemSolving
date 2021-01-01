import unittest
from typing import List, Tuple

def can_place(queens: List[List[bool]], row: int, col: int) -> bool:
    n = len(queens)
    # col check
    for r in range(n):
        if queens[r][col]:
            return False
    # diagonal (top-right) check
    r, c = row - 1, col + 1
    while r >= 0 and r < n and c >= 0 and c < n:
        if queens[r][c]:
            return False        
        r -= 1
        c += 1
    # diagonal (top-left) check
    r, c = row - 1, col - 1
    while r >= 0 and r < n and c >= 0 and c < n:
        if queens[r][c]:
            return False        
        r -= 1
        c -= 1
    # diagonal (bottom-left) check
    r, c = row + 1, col - 1
    while r >= 0 and r < n and c >= 0 and c < n:
        if queens[r][c]:
            return False        
        r += 1
        c -= 1
    # diagonal (bottom-right) check
    r, c = row + 1, col + 1
    while r >= 0 and r < n and c >= 0 and c < n:
        if queens[r][c]:
            return False        
        r += 1
        c += 1
    # row check
    for c in range(n):
        if queens[row][c]:
            return False
    return True

def place_queen(queens: List[List[bool]], row: int, col: int) -> bool:
    if not can_place(queens, row, col):
        return False
    else:
        is_final_state = row == (len(queens) - 1) # if last row, then return as this is final state
        queens[row][col] = True
        if not is_final_state:         
            # check if this is final state
            for c in range(len(queens)):
                if place_queen(queens, row + 1, c):
                    is_final_state = True
                    break

        if not is_final_state: # roll back as this is not valid state
            queens[row][col] = False
         
        return is_final_state

def place_queens(n: int) -> Tuple[Tuple[int]]:
    queens = [[False for _ in range(n)] for _ in range(n)]
    can_place_n_queens = False
    for col in range(n):
        if place_queen(queens, 0, col):
            can_place_n_queens = True
            break
    if can_place_n_queens:
        print("Can place {} queen(s)".format(n))
    else:
        print("Can not place {} queen(s)".format(n))
    result = []
    for i in range(n):
        for j in range(n):
            if queens[i][j]:
                result.append((i, j))
    return tuple(result)

class Tests(unittest.TestCase):
    def test_n_eq_1(self):
        result = place_queens(1)
        self.assertEqual(1, len(result))

    def test_n_eq_2(self):
        result = place_queens(2)
        self.assertEqual(0, len(result)) # cannot place queen in every row

    def test_n_eq_3(self):
        result = place_queens(3)
        self.assertEqual(0, len(result)) # cannot place queen in every row

    def test_n_eq_4(self):
        result = place_queens(4)
        self.assertEqual(4, len(result))

    def test_n_eq_8(self):
        result = place_queens(8)
        self.assertEqual(8, len(result))

    def test_n_eq_16(self):
        result = place_queens(16)
        self.assertEqual(16, len(result))

    # def test_n_eq_32(self): # lengthy operation
    #     result = place_queens(32)
    #     self.assertEqual(32, len(result))

if __name__ == "__main__":
    unittest.main(verbosity = 2)