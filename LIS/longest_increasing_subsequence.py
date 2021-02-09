from typing import List

def len_of_LIS(nums:List[int]) -> int:
    if not nums:
        return 0
    if len(nums) < 2:
        return 1

    lis = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] > lis[-1]:
            lis.append(nums[i])
        else:
            l, r = 0, len(lis) - 1
            while l <= r:
                m = l + ((r - l) >> 2)
                if lis[m] < nums[i]:
                    l = m + 1
                else:
                    r = m - 1
            if 0 <= l < len(lis):
                lis[l] = nums[i]
    return len(lis)