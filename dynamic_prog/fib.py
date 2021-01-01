import unittest

def fib(n):
    if n < 2:
        return n

    n0, n1, n2 = 0, 1, 1
    for _ in range(2, n):
        n2 = n1 + n0
        n1 = n2
        n0 = n1
    return n1 + n0

class Tests(unittest.TestCase):
    def test_ex1(self):
        self.assertEqual(0, fib(0))
    
    def test_ex2(self):
        self.assertEqual(1, fib(1))

    def test_ex3(self):
        self.assertEqual(2, fib(3))

    def test_ex4(self):
        self.assertEqual(8, fib(5))

if __name__ == "__main__":
    unittest.main(verbosity=2)