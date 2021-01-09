from typing import List

def sort_colors(nums:List[int]):
    counter = [0] * 3
    for num in nums:
        counter[num] += 1

    i = 0
    for key, count in enumerate(counter):
        for _ in range(count):
            nums[i] = key
            i += 1

