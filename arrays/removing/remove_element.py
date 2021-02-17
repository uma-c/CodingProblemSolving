from typing import List

def removeElement(nums: List[int], val: int) -> int:
    write_pos = 0
    for num in nums:
        if num != val:
            nums[write_pos] = num
            write_pos += 1
    return write_pos

if __name__ == "__main__":
    nums = [3,2,2,3]
    val = 3
    print(removeElement(nums, val))
    print(nums)