from typing import List
import random

def shuffle(nums: List[int]):
    for i in range(len(nums) - 1, -1, -1):
        r = random.randint(0, i)
        nums[i], nums[r] = nums[r], nums[i]

if __name__ == "__main__":
    A = [1,2,3,4,5,6,7,8,9,10]
    shuffle(A)
    print(A)