from typing import List

def heightChecker(heights: List[int]) -> int:
    hc = sorted(heights.copy())
    m = 0
    for i, h in enumerate(heights):
        if hc[i] != h:
            m += 1
    return m

if __name__ == "__main__":
    heights = [1,1,4,2,1,3]
    #heights = [5,1,2,3,4]
    #heights = [1,2,3,4,5]
    print(heightChecker(heights))