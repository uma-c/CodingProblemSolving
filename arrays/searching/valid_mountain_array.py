from typing import List

def validMountainArray(arr: List[int]) -> bool:
    if not arr or len(arr) < 3:
        return False
    max_e, max_i = float("-inf"), -1
    for i, num in enumerate(arr):
        if num > max_e:
            max_e = num
            max_i = i
    if max_i == 0 or max_i == len(arr) - 1:
        return False
    for i in range(1, max_i):
        if arr[i] <= arr[i - 1]:
            return False
    for i in range(max_i, len(arr) - 1):
        if arr[i + 1] >= arr[i]:
            return False
    return True

if __name__ == "__main__":
    print(validMountainArray([0,3,2,1]))
    print(validMountainArray([3,5,5]))
    print(validMountainArray([0,1,2,3,4,5,6,7,8,9]))
    print(validMountainArray([9,8,7,6,5,4,3,2,1,0]))