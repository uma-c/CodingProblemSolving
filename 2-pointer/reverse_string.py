import unittest

def reverse_string(s: str)->str:
    result = [''] * len(s)
    left, right = 0, len(s) - 1
    while left <= right:
        result[left] = s[right]
        result[right] = s[left]
        left += 1
        right -= 1

    return ''.join(result)

def reverse_string1(s: str)->str:
    return ''.join(reversed(s))

class Tests(unittest.TestCase):
    def test_reverse_string_example1(self):
        str1 = "Hello World"
        result = reverse_string1(str1)
        self.assertEqual("dlroW olleH", result)

    def test_reverse_string_empty_str(self):
        str1 = ""
        result = reverse_string1(str1)
        self.assertEqual("", result)

if __name__ == "__main__":
    unittest.main(verbosity=2)