import unittest
from typing import List

def max_product_of_3(lst: List[int])->int:
    if len(lst) < 3:
        raise ValueError('invalid input')
    sorted_lst = sorted(lst)
    return max(sorted_lst[0] * sorted_lst[1] * sorted_lst[-1], sorted_lst[-1] * sorted_lst[-2] * sorted_lst[-3])

class Tests(unittest.TestCase):
    def test_max_product_of_3_example1(self):
        seq1 = [-1, 9, 22, 3, -15, -7]
        result = max_product_of_3(seq1)
        self.assertEqual(result, -15 * -7 * 22)
    
    def test_max_product_of_3_all_pos(self):
        seq1 = [2, 3, 10, 9, 4, 5]
        result = max_product_of_3(seq1)
        self.assertEqual(result, 10 * 9 * 5)

    def test_max_product_of_3_seq_invalid(self):
        seq1 = [2, 3]
        with self.assertRaises(ValueError):
            max_product_of_3(seq1)
        

if __name__ == "__main__":
    unittest.main(verbosity=2)
