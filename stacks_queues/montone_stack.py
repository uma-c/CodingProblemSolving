from typing import List
import collections

def decreasing_stack(nums:List[int]):
    stack = collections.deque()
    for i, v in enumerate(nums):
        while stack and nums[stack[-1]] <= v:
            stack.pop()
        stack.append(i)
    for i in stack:
        print(nums[i], end=' ')

def increasing_stack(nums:List[int]):
    stack = collections.deque()
    for i, v in enumerate(nums):
        while stack and nums[stack[-1]] >= v:
            stack.pop()
        stack.append(i)
    for i in stack:
        print(nums[i], end=' ')

if __name__ == "__main__":
    increasing_stack([5,3,1,2,4])
    print()
    decreasing_stack([5,3,1,2,4])