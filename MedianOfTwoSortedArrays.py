import math

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        else:
            x, y = len(nums1), len(nums2)
            low, high = 0, x
            sum_of_px_py = (x + y + 1) // 2
            while low <= high:
                partition_x = (low + high) // 2
                partition_y = sum_of_px_py - partition_x
                max_left_x = nums1[partition_x - 1] if 0 < partition_x else -math.inf
                min_right_x = nums1[partition_x] if partition_x < x else math.inf
                max_left_y = nums2[partition_y - 1] if 0 < partition_y else -math.inf
                min_right_y = nums2[partition_y] if partition_y < y else math.inf

                if max_left_x <= min_right_y and max_left_y <= min_right_x: # median is found
                    if  (x + y) % 2 == 0: # even number of elements
                        return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2.0
                    else:
                        return max(max_left_x, max_left_y)
                elif max_left_x > min_right_y:
                    high = partition_x - 1
                else:
                    low = partition_x + 1

if __name__ == '__main__':
    sol = Solution()
    #print(sol.findMedianSortedArrays([1, 4, 6, 8, 10], [2, 7, 11]))
    print(sol.findMedianSortedArrays([1,2], [3,4]))