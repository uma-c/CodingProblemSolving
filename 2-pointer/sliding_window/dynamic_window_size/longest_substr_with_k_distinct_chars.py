import unittest
from math import inf

'''
How sliding window works
------------------------
    expand window until search space is covered
    if desired state is attained
        record state
    reduce window size until desired state is lost
'''
def longest_substr_k_distinct_chars(val: str, k: int)->int:
    window_chars = dict()
    left = 0
    right = 0
    max_len = -inf
    n = len(val)
    while right < n:
        if val[right] in window_chars:
            window_chars[val[right]] += 1
        else:
            window_chars[val[right]] = 1
        if len(window_chars) == k:
            max_len = max(max_len, right - left + 1)
        while len(window_chars) > k and left <= right:            
            window_chars[val[left]] -= 1
            if window_chars[val[left]] == 0:
                window_chars.pop(val[left])
            left += 1
        right += 1
    return max_len

class Tests(unittest.TestCase):
    def test_k_distinct_chars_exist1(self):
        val = "AAAHHBGIP"
        result = longest_substr_k_distinct_chars(val, 2)
        self.assertEqual(result, 5)

    def test_k_distinct_chars_not_exist1(self):
        val = "AAAAAAAAAA"
        result = longest_substr_k_distinct_chars(val, 2)
        self.assertEqual(result, -inf)

unittest.main(verbosity=2)