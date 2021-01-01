import unittest

def reverse_alpha(s: str)->str:
    result = [''] * len(s)
    
    left, right = 0, len(s) - 1
    while left <= right:
        if not s[left].isalpha():
            result[left] = s[left]
            left += 1
        elif not s[right].isalpha():
            result[right] = s[right]
            right -= 1
        else:            
            result[right] = s[left]
            result[left] = s[right]
            left += 1
            right -= 1

    return ''.join(result)

class Tests(unittest.TestCase):
    def test_reverse_alpha_example1(self):
        str1 = "B!FDCEA2"
        result = reverse_alpha(str1)
        self.assertEqual("A!ECDFB2", result)

    def test_reverse_alpha_empty_str(self):
        result = reverse_alpha("")
        self.assertEqual("", result)
    
    def test_reverse_alpha_example2(self):
        str1 = "!@#$%^&*()-+";
        result = reverse_alpha(str1)
        self.assertEqual(str1, result)

if __name__ == "__main__":
    unittest.main(verbosity=2)