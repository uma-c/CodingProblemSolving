from typing import List, Tuple
import unittest

# TC: O(n), SC: O(1)
def find_missing_two1(nums:List[int])->Tuple[int]:
    seqSum, numsSum = 0, 0
    for i in range(1, len(nums) + 3):
        seqSum += i
    
    for num in nums:
        numsSum += num

    pivot = (seqSum - numsSum) // 2
    totalLeftXor, totalRightXor = 0, 0
    for i in range(1, pivot + 1):
        totalLeftXor ^= i
    
    for i in range(pivot + 1, len(nums) + 3):
        totalRightXor ^= i

    numsLeftXor, numsRightXor = 0, 0
    for num in nums:
        if num <= pivot:
            numsLeftXor ^= num
        else:
            numsRightXor ^= num

    return (totalLeftXor ^ numsLeftXor, totalRightXor ^ numsRightXor)

# TC: O(n), SC: O(n)
def find_missing_two(nums:List[int])->Tuple[int]:
    markings = [False] * (len(nums) + 3)
    for num in nums:
        markings[num] = True
    
    missing = []
    for i in range(1, len(markings)):
        if not markings[i]:
            missing.append(i)

    return tuple(missing)

# TC: O(n), SC: O(1)
def find_missing_one1(nums:List[int])->int:
    totalXor, numsXor = 0, 0
    for i in range(1, len(nums) + 2):
        totalXor ^= i

    for num in nums:
        numsXor ^= num

    return totalXor ^ numsXor

# TC: O(n), SC: O(1)
def find_missing_one(nums:List[int])->int:
    n = len(nums) + 1
    seqSum, numsSum = (n * (n+1)) // 2, 0
    for num in nums:
        numsSum += num

    return seqSum - numsSum

class Tests(unittest.TestCase):
    def test_ex1(self):
        lst = [4, 2, 3]
        result = find_missing_two1(lst)
        self.assertTupleEqual((1, 5), result)

    def test_ex2(self):
        lst = [4, 2, 3, 1, 5, 7, 8, 9]
        result = find_missing_two1(lst)
        self.assertTupleEqual((6, 10), result)

    def test_missing_one_ex1(self):
        lst = [1, 2, 3, 4]
        result = find_missing_one(lst)
        self.assertEqual(5, result)

if __name__ == "__main__":
    unittest.main(verbosity=2)