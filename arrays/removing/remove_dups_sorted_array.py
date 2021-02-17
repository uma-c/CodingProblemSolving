from typing import List

def removeDuplicates(nums: List[int]) -> int:
    if not nums:
        return 0
    write_pos = 1
    num = nums[0]
    for i in range(1, len(nums)):
        if num != nums[i]:
            nums[write_pos] = nums[i]
            num = nums[i]
            write_pos += 1
    return write_pos

if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(removeDuplicates(nums))
    print(nums)