from typing import List

# 3 - way partitioning
# ...< p...p p...> p
# equal is partition indexer
def partition(nums: List[int], s:int, e:int) -> int:    
    nums[s], nums[e] = nums[e], nums[s]
    p = nums[e]
    smaller, equal, larger = s, s, e - 1
    while equal <= larger:
        if nums[equal] < p:
            nums[smaller], nums[equal] = nums[equal], nums[smaller] 
            smaller += 1
            equal += 1
        elif nums[equal] == p:
            equal += 1
        else:
            nums[equal], nums[larger] = nums[larger], nums[equal]
            larger -= 1
    nums[equal], nums[e] = nums[e], nums[equal]
    return equal

def partition_reverse(nums: List[int], s:int, e:int) -> int:
    nums[s], nums[e] = nums[e], nums[s]
    p = nums[e]
    larger, equal, smaller = s, s, e - 1
    while equal <= smaller:
        if nums[equal] > p:
            nums[larger], nums[equal] = nums[equal], nums[larger] 
            larger += 1
            equal += 1
        elif nums[equal] == p:
            equal += 1
        else:
            nums[equal], nums[smaller] = nums[smaller], nums[equal]
            smaller -= 1
    nums[equal], nums[e] = nums[e], nums[equal]
    return equal