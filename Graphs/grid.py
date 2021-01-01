from typing import List, Tuple
import unittest

# Grid neighbours
def get_neightbours_updown_left_right_diagonal(r: int, c: int, R: int, C:int)->List[Tuple[int]]:
    rd = [-1, -1, -1, 0, 0, 1, 1, 1] # direction vectors
    cd = [-1, 0, 1, -1, 1, -1, 0, 1] # direction vectors
    result = []
    for i in range(len(rd)):
        rr = r + rd[i]
        cc = c + cd[i]
        if rr < 0 or cc < 0:
            continue
        if rr >= R or cc >= C:
            continue
        result.append((rr, cc))
    return result

# Grid neighbours
def get_neightbours_updown_left_right(r: int, c: int, R:int, C:int)->List[Tuple[int]]:
    rd = [-1, 0, 0, 1]# direction vectors
    cd = [0, -1, 1, 0]# direction vectors
    result = []
    for i in range(len(rd)):
        rr = r + rd[i]
        cc = c + cd[i]
        if rr < 0 or cc < 0:
            continue
        if rr >= R or cc >= C:
            continue
        result.append((rr, cc))
    return result

class Tests(unittest.TestCase):
    def test_neighbours_updown_rightleft1(self):
        result = get_neightbours_updown_left_right(1, 1, 3, 3)
        self.assertEqual([(0, 1), (1, 0), (1, 2), (2, 1)], result)

    def test_neighbours_updown_rightleft2(self):
        result = get_neightbours_updown_left_right(1, 1, 2, 2)
        self.assertEqual([(0, 1), (1, 0)], result)

    def test_neighbours_updown_rightleft_diagonal1(self):
        result = get_neightbours_updown_left_right_diagonal(1, 1, 3, 3)
        self.assertEqual([(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)], result)

    def test_neighbours_updown_rightleft_diagonal2(self):
        result = get_neightbours_updown_left_right_diagonal(1, 1, 2, 2)
        self.assertEqual([(0, 0), (0, 1), (1, 0)], result)

if __name__ == "__main__":
    unittest.main(verbosity = 2)