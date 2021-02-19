from typing import List

def findDisappearedNumbers(nums: List[int]) -> List[int]:
    for num in nums:
        if num < 0:
            idx = - num - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
        else:
            idx = num - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
    d = []
    for i, num in enumerate(nums):
        if num > 0:
            d.append(i + 1)
    return d

if __name__ == "__main__":
    nums = [4,3,2,7,8,2,3,1]
    print(findDisappearedNumbers(nums))