import unittest

def is_subsequence(s: str, t: str) -> bool:
    if len(s) > len(t):
        return False

    if len(s) < 1:
        return True

    i = 0
    j = 0
    while j < len(t) and i < len(s):
        if t[j] == s[i]:
            i += 1
        j += 1
        
    return i == len(s)

class Tests(unittest.TestCase):
    def test_ex1(self):
        s = "ace"
        t = "abcde"
        self.assertTrue(is_subsequence(s, t))

    def test_ex2(self):
        s = "aec"
        t = "abcde"
        self.assertFalse(is_subsequence(s, t))

if __name__ == "__main__":
    unittest.main(verbosity=2)