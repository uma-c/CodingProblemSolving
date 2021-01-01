from typing import List
import unittest

def max_sum_subarray(arr:List[int], k: int)->int:
    if k < 1:
        raise ValueError('k must be non-zero positive integer')
    current_sum = 0    
    for i in range(k):
        current_sum += arr[i]
    max_sum = current_sum
    left, right = 0, k
    while right < len(arr):
        current_sum += arr[right] - arr[left]
        max_sum = max(current_sum, max_sum)
        left += 1
        right += 1
    return max_sum

class Tests(unittest.TestCase):
    def test_sum_3(self):
        arr = [4, 2, 1, 7, 8, 1, 7, 5, 2, 0]
        sum_3 = max_sum_subarray(arr, 3)
        self.assertEqual(sum_3, 16)

    def test_sum_1(self):
        arr = [4, 2, 1, 7, 8, 1, 7, 5, 2, 0]
        sum_1 = max_sum_subarray(arr, 1)
        self.assertEqual(sum_1, 8)

    def test_sum_all_negative_elements(self):
        arr = [-4, -2, -1, -7, -8, -1, -7, -5, -2]
        sum_3 = max_sum_subarray(arr, 3)
        self.assertEqual(sum_3, -7)

    def test_k_0(self):
        arr = [-4, -2, -1, -7, -8, -1, -7, -5, -2]
        with self.assertRaises(ValueError):
            max_sum_subarray(arr, 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)