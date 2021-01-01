from typing import List
import unittest

def set_next_greater_element(greater_nums: List[int], stack: List[int]):
    for i in range(len(greater_nums) - 1, -1, -1):
        if len(stack) > 0:
            if stack[-1] > greater_nums[i]:
                greater_nums[i] = stack[-1]
            else:
                k = stack.pop()
                while len(stack) > 0 and k > greater_nums[i]:
                    k = stack.pop()
                greater_nums[i] = k if k > greater_nums[i] else -1
        else:            
            stack.append(greater_nums[i])
            greater_nums[i] = -1

def get_next_greater_element(nums: List[int]) -> List[int]:
    if len(nums) < 1:
        return []

    stack = []
    result = nums.copy()
    set_next_greater_element(result, stack)
    set_next_greater_element(result, stack)
    return result


class Test(unittest.TestCase):
    def test_example1(self):
        a = get_next_greater_element([1, 2, 1])
        self.assertEqual(a, [2, -1, 2])
    
    def test_example2(self):
        a = get_next_greater_element([1, 2, 3])
        self.assertEqual(a, [2, 3, -1])

    def test_example3(self):
        a = get_next_greater_element([5, 4, 3, 2, 1])
        self.assertEqual(a, [-1,5,5,5,5])

unittest.main(verbosity=2)