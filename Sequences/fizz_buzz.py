import unittest

def fizz_buzz(n: int)->str:
    result = []
    for i in range(1, n+1, 1):
        result.append(str(i))

    for i in range(3, n+1, 3):
        result[i - 1] = "fizz"

    for i in range(5, n+1, 5):
        result[i - 1] = "buzz"
    
    for i in range(15, n+1, 15):
        result[i - 1] = "fizzbuzz"

    return ''.join(result)

class Tests(unittest.TestCase):
    def test_reverse_string_example1(self):
        result = fizz_buzz(15)
        self.assertEqual("12fizz4buzzfizz78fizzbuzz11fizz1314fizzbuzz", result)

    def test_reverse_string_example2(self):
        result = fizz_buzz(9)
        self.assertEqual("12fizz4buzzfizz78fizz", result)

if __name__ == "__main__":
    unittest.main(verbosity=2)