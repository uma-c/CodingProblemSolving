from typing import List

def replaceElements(arr: List[int]) -> List[int]:
    if not arr:
        return arr
    max_e = arr[-1]
    arr[-1] = -1
    for i in range(len(arr) - 2, -1, -1):
        temp = max_e
        if arr[i] > max_e:
            max_e = arr[i]
        arr[i] = temp
    return arr

if __name__ == "__main__":
    arr = [17,18,5,4,6,1]
    print(replaceElements(arr))        