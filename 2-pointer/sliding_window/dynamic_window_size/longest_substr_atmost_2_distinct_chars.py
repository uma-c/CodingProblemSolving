'''
LC 340/LC 159
'''
import unittest

def longest_substr_distinct_chars(s:str, k:int)->int:
    if s is None or len(s) < 1:
        return 0
    
    i = j = 0
    state = dict()
    n = len(s)
    max_l = 0
    while j < n:
        if s[j] in state:
            state[s[j]] += 1
        else:
            state[s[j]] = 1

        while len(state) > k:
            state[s[i]] -= 1
            if state[s[i]] == 0:
                state.pop(s[i])
            i += 1
        max_l = max(max_l, j - i + 1)
        j += 1
    return max_l

class Tests(unittest.TestCase):
    def test_ex1(self):
        s = "eceba"
        k = 2
        result = longest_substr_distinct_chars(s, k)
        self.assertEqual(3, result)

    def test_ex2(self):
        s = "ccaabbb"
        k = 2
        result = longest_substr_distinct_chars(s, k)
        self.assertEqual(5, result)

if __name__ == "__main__":
    unittest.main(verbosity = 2)
