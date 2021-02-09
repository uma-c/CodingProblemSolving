from typing import List

# Time complexity: O(n), Space complexity: O(n)
def zero_sum_subarray(nums:List[int]) -> List[int]:    
    s = nums[0]
    sums = { s : 0 }
    for i in range(1, len(nums)):
        s += nums[i]
        if sum == 0:
            return [0, i]
        elif s in sums:
            return [sums.get(s) + 1 , i]
        else:
            sums[s] = i
    return None

if __name__ == "__main__":
    print(zero_sum_subarray([1, 2, -5, 1, 2, -1]))