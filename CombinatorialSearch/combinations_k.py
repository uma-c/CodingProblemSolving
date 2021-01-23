from typing import List

def backtrack(nums, k, start, track, result):
    if k == len(track):
        result.append(track.copy())

    for i in range(start, len(nums)):
        track.append(nums[i])
        backtrack(nums, k, i + 1, track, result)
        track.pop(-1)

def combinations(nums:List[int], k:int):
    result = []
    backtrack(nums, k, 0, [], result)
    return result

if __name__ == "__main__":
    print(combinations([1,2,3,4,5], 2))