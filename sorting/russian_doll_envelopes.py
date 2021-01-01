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
    
    se = []
    for e in envelopes:
        se.append([e[0], e[0] - e[1], e[1]])
    se.sort()
    dp = [se[0]]
    for i in range(1, len(se)):
        if dp[-1][0] < se[i][0] and dp[-1][2] < se[i][2]:
            dp.append(se[i])
        else:
            l, r = 0, len(dp) - 1
            while l <= r:
                m = l + (r - l) // 2
                if dp[m][2] < se[i][2]:
                    l = m + 1
                else:
                    r = m - 1
            if 0 <= l < len(dp):
                dp[l] = se[i]
    return len(dp)

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

    # def test_lis(self):
    #     nums = [5, 3, 7, 4, 2, 9]
    #     result = lis(nums)
    #     print(result)
    #     self.assertEqual(3, len(result))

if __name__ == "__main__":
    unittest.main(verbosity = 2)