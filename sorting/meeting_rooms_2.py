'''
253. Meeting Rooms II
Given an array of meeting time intervals consisting of start and end times[[s1,e1],[s2,e2],...](si< ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]

Output:1
'''
from typing import List
import unittest

def min_meeting_rooms(intervals:List[List[int]]) -> int:
    events = [(it[0], 1) for it in intervals] + [(it[1], -1) for it in intervals]
    events.sort()
    rooms = 0
    max_concurrent = 0
    for e in events:
        rooms += e[1]
        max_concurrent = max(rooms, max_concurrent)
    return max_concurrent    

class Tests(unittest.TestCase):
    def test_ex1(self):
        self.assertEqual(2, min_meeting_rooms([[0, 30], [5, 10], [15, 20]]))

    def test_ex2(self):
        self.assertEqual(1, min_meeting_rooms([[7, 10], [2, 4]]))

if __name__ == "__main__":
    unittest.main(verbosity = 2)