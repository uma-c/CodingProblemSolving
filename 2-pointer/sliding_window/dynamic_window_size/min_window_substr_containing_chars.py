from collections import Counter
import unittest

def min_window_substr(s:str, t:str)->str:
    desired_state = Counter(t)
    state = Counter()
    formed = 0
    required = len(desired_state)
    i = j = 0
    min_window = float("inf"), None
    while j < len(s):
        char = s[j]
        if char in desired_state:
            state[char] += 1
            if state[char] == desired_state[char]:
                formed += 1

        while i <= j and formed == required:
            char = s[i]
            if j - i + 1 < min_window[0]:
                min_window = j - i + 1, i
            if char in desired_state:
                state[char] -= 1
                if state[char] == desired_state[char] - 1:
                    formed -= 1
            i += 1
        j += 1
    return "" if min_window[0] == float("inf") else s[min_window[1] : min_window[1] + min_window[0]]

class Tests(unittest.TestCase):
    def test_example1(self):
        result = min_window_substr("ADOBECODEBANC", "ABC")
        self.assertEqual("BANC", result)

    def test_example2(self):
        result = min_window_substr("DEFG", "ABC")
        self.assertEqual("", result)

    def test_example3(self):
        result = min_window_substr("ABABCAAB", "AA")
        self.assertEqual("AA", result)

if __name__ == "__main__":
    unittest.main(verbosity=2)