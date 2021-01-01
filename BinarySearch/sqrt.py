import unittest

def sqrt(x:int) -> int:
    l, r = 0, x
    while l <= r:
        m = l + (r - l) // 2
        sq_m = m * m
        if sq_m == x:
            return m
        elif sq_m > x:
            r = m - 1
        else:
            l = m + 1
    return r

class Tests(unittest.TestCase):
    def test_ex1(self):
        self.assertEqual(2, sqrt(4))

    def test_ex2(self):
        self.assertEqual(2, sqrt(8))

if __name__ == "__main__":
    unittest.main(verbosity = 2)