from typing import List

def moveZeroes(nums: List[int]) -> None:
    write_pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[write_pos] = nums[i]
            write_pos += 1
    for i in range(write_pos, len(nums)):
        nums[i] = 0

if __name__ == "__main__":
    nums = [0,1,0,3,12]
    moveZeroes(nums)
    print(nums)