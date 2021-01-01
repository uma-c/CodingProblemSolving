import unittest

def longest_repeating_char_replace(s:str, k:int) -> int:
    if s is None or len(s) < 1:
        return 0

    i = j = 0
    max_l = 0
    n = len(s)
    state = dict()
    while j < n:
        if s[j] in state:
            state[s[j]] += 1
        else:
            state[s[j]] = 1
        while i < j and (j - i + 1 - max(state.values())) > k:
            state[s[i]] -= 1
            if state[s[i]] == 0:
                state.pop(s[i])
            i += 1        
        max_l = max(max_l, j - i + 1)
        j += 1
    return max_l

class Tests(unittest.TestCase):
    def test_ex1(self):
        s = "ABAB"
        k = 2
        result = longest_repeating_char_replace(s, k)
        self.assertEqual(4, result)

    def test_ex2(self):
        s = "AABABBA"
        k = 1
        result = longest_repeating_char_replace(s, k)
        self.assertEqual(4, result)

    def test_ex3(self):
        s = "KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF"
        k = 4
        result = longest_repeating_char_replace(s, k)
        self.assertEqual(7, result)

if __name__ == "__main__":
    unittest.main(verbosity = 2)