'''
You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Note:
Rotation is not allowed.

Example:

Input: [[5,4],[6,4],[6,7],[2,3]]
Output: 3 
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).


1 3 5

2
'''
from typing import List
import unittest

def max_envelopes(envelopes:List[List[int]]) -> int:
    if envelopes is None or len(envelopes) < 1:
        return 0

    # this is core idea; sort by width and if width matches, then descending order of height
    envelopes.sort(key=lambda ae:[ae[0], ae[0] - ae[1]])
    lis = [envelopes[0]]
    for i in range(1, len(envelopes)):
        if lis[-1][0] < envelopes[i][0] and lis[-1][1] < envelopes[i][1]:
            lis.append(envelopes[i])
        else:
            l, r = 0, len(lis) - 1
            while l <= r:
                m = l + (r - l) // 2
                if lis[m][1] < envelopes[i][1]:
                    l = m + 1
                else:
                    r = m - 1
            if 0 <= l < len(lis):
                lis[l] = envelopes[i]
    return len(lis)

class Tests(unittest.TestCase):
    def test_ex1(self):
        e = [[5,4],[6,4],[6,7],[2,3]]
        self.assertEqual(3, max_envelopes(e))

    def test_ex2(self):
        e = [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
        self.assertEqual(5, max_envelopes(e))

    def test_ex3(self):
        e = [[46,89],[50,53],[52,68],[72,45],[77,81]]
        self.assertEqual(3, max_envelopes(e))

    def test_ex4(self):
        e = [[30,50],[12,2],[3,4],[12,15]]
        self.assertEqual(3, max_envelopes(e))

    def test_ex5(self):
        e = [[1,2],[2,3],[3,4],[3,5],[4,5],[5,5],[5,6],[6,7],[7,8]]
        self.assertEqual(7, max_envelopes(e))

if __name__ == "__main__":
    unittest.main(verbosity = 2)