from typing import List
import unittest
import collections

def find_all_anagrams(s:str, p:str)->List[int]:
    i = 0
    n = len(s)
    t = collections.Counter(p)
    state = collections.Counter()
    formed = 0
    required = len(t)
    anagrams = []
    for k in range(len(p) - 1):
        state[s[k]] += 1
        if state[s[k]] == t[s[k]]:
            formed += 1

    for j in range(len(p) - 1, n):        
        state[s[j]] += 1
        if state[s[j]] == t[s[j]]:
            formed += 1        
        if formed == required:
            anagrams.append(i)
        state[s[i]] -= 1
        if state[s[i]] == t[s[i]] - 1:
            formed -= 1
        i += 1

    return anagrams

class Tests(unittest.TestCase):
    def test_ex1(self):
        s = "cbaebabacd"
        p = "abc"
        result = find_all_anagrams(s, p)
        self.assertEqual([0, 6], result)

if __name__ == "__main__":
    unittest.main(verbosity = 2)