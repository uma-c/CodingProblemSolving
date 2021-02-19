from typing import List
import heapq

def thirdMax(nums: List[int]) -> int:
    '''
    Quick-Select
    PriorityQueue
    Heap
    Linear-Search
    Sort
    '''
    nums_set = set(nums)
    if len(nums_set) < 3:
        return max(nums_set)
    a, b, c = float("-inf"), float("-inf"), float("-inf")
    for num in nums_set:
        if num > c:
            c, b, a = num, c, b             
        elif num > b:
            b, a = num, b
        elif num > a:
            a = num
    return a if a != float("-inf") else c

if __name__ == "__main__":
    nums = [2,2,3,1]
    #nums = [1, 1, 2]
    print(thirdMax(nums))