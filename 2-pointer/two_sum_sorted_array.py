from typing import List
import unittest

def find_two_sum(numbers:List[int], target:int)->List[int]:
    if numbers is None or len(numbers) < 1:
        return [None, None]
    i, j = 0, len(numbers) - 1
    while i < j:
        two_sum  = numbers[i] + numbers[j]
        if two_sum == target:
            return [i, j]
        elif two_sum < target:
            i += 1
        else:
            j -= 1        

    return [None, None]

class Tests(unittest.TestCase):
    def test_ex1(self):
        A = [2, 7, 11, 15]
        result = find_two_sum(A, 9)
        self.assertEqual([0, 1], result)

    def test_ex2(self):
        A = [6, 9, 11, 17]
        result = find_two_sum(A, 26)
        self.assertEqual([1, 3], result)

    def test_ex3(self):
        A = [6, 9, 11, 17]
        result = find_two_sum(A, 27)
        self.assertEqual([None, None], result)

    def test_ex4(self):
        A = []
        result = find_two_sum(A, 12)
        self.assertEqual([None, None], result)

if __name__ == "__main__":
    unittest.main(verbosity = 2)