'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

'''
from collections import Counter
import unittest

def valid_anagrams(s:str, t:str) -> bool:
    if len(s) != len(t):
        return False
    
    counter_s = Counter(s)
    for c in t:
        counter_s[c] -= 1
    
    for val in counter_s.values():
        if val != 0:
            return False
    return True

class Tests(unittest.TestCase):
    def test_ex1(self):
        self.assertTrue(valid_anagrams("anagram", "nagaram"))

if __name__ == "__main__":
    unittest.main(verbosity = 2)

