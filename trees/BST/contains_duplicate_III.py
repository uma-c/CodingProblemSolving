from typing import List

def containsNearbyAlmostDuplicate(nums: List[int], k: int, t: int) -> bool:
    def inRange(num):
        bn = num // (t + 1)
        buckets_to_check = [bn - 1, bn, bn + 1]
        for b in buckets_to_check:
            if b in buckets:
                if abs(num - buckets[b]) <= t:
                    return True
        if bn not in buckets or buckets[bn] < num:             
            buckets[bn] = num
        return False    
    n = len(nums)
    if n < 2:
        return False    
    buckets = dict()
    k = min(k, n)
    i = 0
    while i < k:
        #print("i=", i)     
        if inRange(nums[i]):
            return True
        i += 1
    if i < n:
        #print("i=", i)
        if inRange(nums[i]):
            return True
        i += 1
    j = 0
    while i < n:
        #print("i=", i, "i - j - 1=", i - j - 1)
        if i - j == k + 1:
            #print("j=", j)
            bn = nums[j] // (t + 1)
            buckets[bn] = float("-inf")
        if inRange(nums[i]):
            return True
        j += 1
        i += 1
    return False

if __name__ == "__main__":
    # nums = [1,2,3,1]
    # k = 3
    # t = 0
    # nums = [1,0,1,1]
    # k = 1
    # t = 2
    # nums = [1,5,9,1,5,9]
    # k = 2
    # t = 3
    # nums = [8,7,15,1,6,1,9,15]
    # k = 1
    # t = 3
    # nums = [2147483646,2147483647]
    # k = 3
    # t = 3
    # nums = [-3, 3]
    # k = 2
    # t = 4
    nums = [2,0,-2,2]
    k = 2
    t = 1
    print(containsNearbyAlmostDuplicate(nums, k, t))