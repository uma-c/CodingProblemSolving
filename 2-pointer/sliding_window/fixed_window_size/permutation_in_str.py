import unittest
from collections import Counter

def permuation_exist(s1:str, s2:str) -> bool:
    if len(s1) > len(s2):
        return 0

    i = 0
    s1_state = Counter(s1)
    s2_state = Counter()
    req = len(s1_state)
    formed = 0
    for k in range(len(s1) - 1):
        s2_state[s2[k]] += 1
        if s2_state[s2[k]] == s1_state[s2[k]]:
            formed += 1

    for j in range(len(s1) - 1, len(s2)):
        s2_state[s2[j]] += 1
        if s2_state[s2[j]] == s1_state[s2[j]]:
            formed += 1
        if formed == req:
            return True
        s2_state[s2[i]] -= 1
        if s2_state[s2[i]] == s1_state[s2[i]] - 1:
            formed -= 1
        i += 1

    return False

class Tests(unittest.TestCase):
    def test_ex1(self):
        s1 = "ab"
        s2 = "eidbaooo"
        self.assertEqual(True, permuation_exist(s1, s2))

    def test_ex2(self):
        s1 = "ab"
        s2 = "eidboaoo"
        self.assertEqual(False, permuation_exist(s1, s2))

if __name__ == "__main__":
    unittest.main(verbosity = 2)