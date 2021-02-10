'''
480. Sliding Window Median
Hard

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].

Note:
You may assume k is always valid, ie: k is always smaller than input array's size for non-empty array.
Answers within 10^-5 of the actual value will be accepted as correct.
'''
from typing import List
import heapq

def median_of_sliding_window(nums: List[int], k: int) -> List[float]:
    result = []
    min_heap = []
    max_heap = []
    for i in range(len(nums)):
        if len(max_heap) <= len(min_heap):
            heapq.heappush(min_heap, nums[i])
            val = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -val)
        else:
            heapq.heappush(max_heap, -nums[i])
            val = heapq.heappop(max_heap)
            heapq.heappush(min_heap, -val)
        
        if len(max_heap) + len(min_heap) == k:
            print(max_heap, min_heap)
            if len(max_heap) == len(min_heap):
                result.append((min_heap[0] - max_heap[0]) / 2)                
            else:
                result.append(-max_heap[0] if len(max_heap) > len(min_heap) else min_heap[0])
            j = i - k + 1
            if nums[j] in min_heap:
                min_heap.remove(nums[j])
                heapq.heapify(min_heap)
            else:
                max_heap.remove(-nums[j])
                heapq.heapify(max_heap)
    return result

def median_of_sliding_window1(nums: List[int], k: int) -> List[float]:
    result = []
    mp = (k // 2) + 1
    for i in range(k - 1, len(nums)):
        ordered_window = heapq.nsmallest(mp, nums[i - k + 1:i+1])
        if k % 2: # odd
            result.append(ordered_window[-1])
        else: # even
            result.append((ordered_window[-1] + ordered_window[-2]) / 2)
    return result

if __name__ == "__main__":
    print(median_of_sliding_window([7,0,3,9,9,9,1,7,2,3], 6))