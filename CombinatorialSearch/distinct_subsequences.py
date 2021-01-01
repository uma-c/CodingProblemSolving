'''
Given a string S, count the number of distinct, non-empty subsequences of S .

Since the result may be large, return the answer modulo 10^9 + 7.
 

Example 1:

Input: "abc"
Output: 7
Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".
Example 2:

Input: "aba"
Output: 6
Explanation: The 6 distinct subsequences are "a", "b", "ab", "ba", "aa" and "aba".
Example 3:

Input: "aaa"
Output: 3
Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".

'''
import unittest
import collections

'''
C(ith char) = C((i - 1) chars) * 2 + 1 - repetitions
repetitions = C(char previously seen) + 1
'''
def distinct_subsequences(S:str)->int:
    if S is None or len(S) < 1:
        return 0
    counter = collections.Counter()
    result = 0
    for c in S:        
        result, counter[c] = result * 2 + 1 - counter[c], result + 1
    return result % 1000000007

class Tests(unittest.TestCase):
    def test_ex1(self):
        self.assertEqual(3, distinct_subsequences("aaa"))

    def test_ex2(self):
        self.assertEqual(7, distinct_subsequences("abc"))

    def test_ex3(self):
        self.assertEqual(6, distinct_subsequences("aba"))

    def test_ex4(self):
        self.assertEqual(5, distinct_subsequences("lee"))

if __name__ == "__main__":
    unittest.main(verbosity = 2)