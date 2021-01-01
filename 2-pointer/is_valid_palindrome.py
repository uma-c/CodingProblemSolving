import unittest

def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if not s[left].isalpha():
            left += 1
        elif not s[right].isalpha():
            right -= 1
        elif s[left].lower() == s[right].lower():
            left += 1
            right -= 1
        else:
            return False
    return True

class Tests(unittest.TestCase):
    def test_valid_palindrome1(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_invalid_palindrome1(self):
        self.assertFalse(is_palindrome("bru"))

    def test_valid_palindrome2(self):
        self.assertTrue(is_palindrome("A Santa Lived As a Devil At NASA"))

if __name__ == "__main__":
    unittest.main(verbosity=2)