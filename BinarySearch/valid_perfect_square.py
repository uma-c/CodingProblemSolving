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
    if 0 <= num < 2:
        return True
    elif num < 0:
        return False
    x = num // 2
    while x * x > num:
        x = (x + num // x) // 2
    return x * x == num

class Tests(unittest.TestCase):
    def test_ex1(self):
        self.assertTrue(is_perfect_square(16))

    def test_ex2(self):
        self.assertFalse(is_perfect_square(14))

if __name__ == "__main__":
    unittest.main(verbosity = 2)