from typing import List
import sys

sys.path.append('C:/U/github/CodingProblemSolving/sorting')
sys.path.append('C:/U/github/CodingProblemSolving/Sequences')

from partition import partition
from knuth_shuffle import shuffle

def qsort(nums: List[int], i: int, j: int):
    if i < j:
        p = partition(nums, i, j)
        qsort(nums, i, p - 1)
        qsort(nums, p + 1, j)

def quick_sort(nums: List[int]):
    shuffle(nums)
    qsort(nums, 0, len(nums) - 1)

if __name__ == "__main__":
    nums = [4, 8, 6, 5, 9, 1, 3, 7, 2]
    quick_sort(nums)
    print(nums)