from typing import List

def bsearch(nums: List[int], t:int) -> int:
    l, r = 0, len(nums) - 1    
    while (l <= r):
        m = l + ((r - l) // 2)
        if nums[m] == t:
            return m
        elif nums[m] < t:
            l = m + 1
        else:
            r = m - 1

    return -1