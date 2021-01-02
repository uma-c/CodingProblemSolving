'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
'''

from typing import List
import unittest

def merge_intervals(intervals:List[List[int]]) -> List[List[int]]:
    if intervals is None or len(intervals) < 2:
        return intervals
    sorted_intervals = sorted(intervals)
    result = []
    curr = sorted_intervals[0]
    for i in range(1, len(sorted_intervals)):
        interval = sorted_intervals[i]
        if interval[0] <= curr[1]:
            curr[1] = max(curr[1], interval[1])
        else:
            result.append(curr)
            curr = interval

    result.append(curr)
    return result

class Tests(unittest.TestCase):
    def test_ex1(self):
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        result = merge_intervals(intervals)
        self.assertEqual([[1,6],[8,10],[15,18]], result)

if __name__ == "__main__":
    unittest.main(verbosity = 2)