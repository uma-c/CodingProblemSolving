import unittest
from typing import List, Tuple

def merge_intervals(intervals: List[Tuple[int]]) -> List[Tuple[int]]:
    if len(intervals) < 1:
        return []

    sorted_intervals = sorted(intervals)
    result = []
    curr_interval = [sorted_intervals[0][0], sorted_intervals[0][1]]
    n = len(sorted_intervals)
    for i in range(1, n):
        interval = sorted_intervals[i]
        if interval[0] <= curr_interval[1]:
            curr_interval[1] = max(curr_interval[1], interval[1])
        else:
            result.append(tuple(curr_interval))
            curr_interval = [interval[0], interval[1]]

    result.append(tuple(curr_interval))
    return result

class Tests(unittest.TestCase):
    def test_merge_intervals_example1(self):
        intervals = [(10, 13), (12, 25), (4, 32), (7, 15), (2, 8), (9, 35)]
        result = merge_intervals(intervals)
        self.assertEqual(result, [(2, 35)])

    def test_merge_intervals_example2(self):
        intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]
        result = merge_intervals(intervals)
        self.assertEqual(result, [(1, 6), (8, 10), (15, 18)])        

    def test_merge_intervals_empty_list(self):
        intervals = []
        result = merge_intervals(intervals)
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main(verbosity=2)