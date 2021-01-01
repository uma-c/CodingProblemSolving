'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

Example 1:

Input: num = 16
Output: true
Example 2:

Input: num = 14
Output: false
 

Constraints:

1 <= num <= 2^31 - 1
'''
import unittest

def is_perfect_square(num:int) -> bool:
    if num < 0:
        return False

    l, r = 1, num
    while l <= r:
        m = l + (r - l) // 2
        sqr = m * m
        if sqr == num:
            return True
        elif sqr > num:
            r = m - 1
        else:
            l = m + 1

    return False

class Tests(unittest.TestCase):
    def test_ex1(self):
        self.assertTrue(is_perfect_square(16))

    def test_ex2(self):
        self.assertFalse(is_perfect_square(14))

if __name__ == "__main__":
    unittest.main(verbosity = 2)