from typing import List
import unittest
'''
1 2 3 => 

1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
'''
def _permute(nums: List[int]):
    if nums is None or len(nums) <= 1:
        yield nums
    else:
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for p in _permute(nums[:i] + nums[i+1:]):            
                yield nums[i:i+1] + p

def permute(nums: List[int]) -> List[List[int]]:
    nums.sort()
    return list(_permute(nums))

'''
Steinhaus-Johnson-Trotter algorithm
Time complexity: O(n!), Space complexity: O(n!)
'''
def permute1(nums: List[int]) -> List[List[int]]:
    if nums is None or len(nums) < 1:
        return nums
    i_perms = [[nums[0]]]
    perms = i_perms
    for pos in range(1, len(nums)):
        num = nums[pos]
        perms = []
        perm_set = set()
        for p, perm in enumerate(i_perms):
            iter_range = range(pos, -1, -1) if (p % 2) else range(pos + 1)            
            for i in iter_range:
                new_perm = [None] * (pos + 1)
                perm_txt = [''] * (pos + 1)
                j = 0
                while j < i:
                    new_perm[j] = perm[j]
                    perm_txt[j] = str(perm[j])
                    j += 1
                new_perm[j] = num
                perm_txt[j] = str(num)
                while j < pos:
                    new_perm[j + 1] = perm[j]
                    perm_txt[j + 1] = str(perm[j])
                    j += 1
                perm_txt = ''.join(perm_txt)
                if not (perm_txt in perm_set):
                    perms.append(new_perm)
                    perm_set.add(perm_txt)
        i_perms = perms
    return perms


class Tests(unittest.TestCase):
    def test_ex1(self):
        nums = [1, 2, 3]
        result = list(permute(nums))
        self.assertListEqual([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]], result)

    def test_ex2(self):
        nums = [1]
        result = list(permute(nums))
        self.assertListEqual([[1]], result)

    def test_ex_dups1(self):
        nums = [2,1,2]
        self.assertListEqual([[1, 2, 2], [2, 1, 2], [2, 2, 1]], permute(nums))


if __name__ == "__main__":
    unittest.main(verbosity=2)
