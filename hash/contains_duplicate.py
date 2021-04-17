from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    s = set(nums)
    return len(s) != len(nums)