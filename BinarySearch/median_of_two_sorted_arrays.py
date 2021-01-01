from typing import List
import unittest
'''
partition arrays such that no. of elements in left partition = no. of elements in right partition
'''
class SubArray(object):
    def __init__(self, A:List[int], start:int, n:int):
        self.arr = A
        self.set(start, n)
    
    def set(self, start, n):
        if (start + n - 1) < len(self.arr):
            self.start = start
            self.size = n
        else:
            raise ValueError("Invalid input")

def median_of_array(A:List[int]) -> int:
    mid = (len(A) - 1) // 2
    if len(A) % 2 == 0: # even number of elements
        return (A[mid] + A[mid + 1]) / 2
    else: # odd number of elements
        return A[mid]

def median_of_subarray(A:SubArray):
    mid = A.start + (A.size - 1) // 2
    if A.size % 2 == 0: # even number of elements
        return (A.arr[mid] + A.arr[mid + 1]) / 2
    else: # odd number of elements
        return A.arr[mid]

def merge_subarrays(A:SubArray, B:SubArray) -> List[int]:
    temp = []
    a, b = A.start, B.start
    a_end, b_end = a + A.size - 1, b + B.size - 1
    while a <= a_end and b <= b_end:
        if A.arr[a] <= B.arr[b]:
            temp.append(A.arr[a])
            a += 1
        else:
            temp.append(B.arr[b])
            b += 1
        
    while a <= a_end:
        temp.append(A.arr[a])
        a += 1

    while b <= b_end:
        temp.append(B.arr[b])
        b += 1
        
    return temp    

def median_of_subarrays(A:SubArray, B:SubArray) -> int:
    if A.size > B.size:
        return median_of_subarrays(B, A)

    while A.size > 0:
        # from i and j right starts in A and B
        i = A.start + A.size // 2
        j = ((len(A.arr) + len(B.arr) + 1) // 2) - i
        max_left_A = A.arr[i - 1] if i > 0 else float("inf")
        max_left_B = B.arr[j - 1] if j > 0 else float("inf")
        min_right_A = A.arr[i] if i < len(A.arr) else float("-inf")
        min_right_B = B.arr[j] if j < len(B.arr) else float("-inf")
        # max(left of A) <= min(right of B) and max(left of B) <= min(right of A)
        if max_left_A <= min_right_B and max_left_B <= min_right_A:
            if (len(A.arr) + len(B.arr)) % 2 == 0: # even number of elements
                return (max(max_left_A, max_left_B) + min(min_right_A, min_right_B)) / 2
            else: # odd number of elements
                return min(min_right_A, min_right_B)
        # max left of A > min of right of B, move towards left of A and right of B
        elif max_left_A > min_right_B: 
            A.set(A.start, A.size // 2)
            if j < len(B.arr) - 1:
                B.set(j + 1, B.size // 2)
            else:
                return median_of_subarray(A)
        # max left of B > min right of A
        elif max_left_B > min_right_A: # move towards right of A and left of B            
            B.set(B.start, B.size // 2)
            if i < len(A.arr) - 1:
                A.set(i + 1, A.size // 2)
            else:
                return median_of_subarray(B)
        else:
            break

    return median_of_subarray(B) # since A is not contributing elements

# def median(A:List[int], B:List[int]) -> int:
#     if (A is None or len(A) < 1) and (B is None and len(B) < 1):
#         raise ValueError("invalid input")
#     return median_of_subarrays(SubArray(A, 0, len(A)), SubArray(B, 0, len(B)))    

def median(A:List[int], B:List[int]) -> int:
    if (A is None or len(A) < 1) and (B is None and len(B) < 1):
        raise ValueError("invalid input")
    
    if len(A) > len(B):
        return median(B, A)

    if len(A) > 0:
        start, end, mid = 0, len(A), ((len(A) + len(B) + 1) // 2)
        while start <= end:
            i = start + (end - start) // 2
            j = mid - i
            max_left_A = A[i - 1] if i > 0 else float("-inf")
            max_left_B = B[j - 1] if j > 0 else float("-inf")
            min_right_A = A[i] if i < len(A) else float("inf")
            min_right_B = B[j] if j < len(B) else float("inf")   
            if max_left_A <= min_right_B and max_left_B <= min_right_A:
                if (len(A) + len(B)) % 2 == 0: # even number of elements
                    return (max(max_left_A, max_left_B) + min(min_right_A, min_right_B)) / 2
                else: # odd number of elements
                    return max(max_left_A, max_left_B)     
            elif max_left_A > min_right_B: # move towards left of A
                end = i - 1
            else: #if max_left_B > min_right_A: move towards right of A
                start = i + 1
    
    return median_of_array(B)

class Tests(unittest.TestCase):
    def test_ex1(self):
        A = [1, 3, 5]
        B = [2, 4, 6]
        m = median(A, B)
        self.assertEqual(3.5, m)

    def test_ex2(self):
        A = []
        B = [1, 2, 3]
        m = median(A, B)
        self.assertEqual(2, m)

    def test_ex3(self):
        A = [1, 2, 3, 4]
        B = []
        m = median(A, B)
        self.assertEqual(2.5, m)

    def test_ex4(self):
        B = [3, 4]
        A = [1, 2, 5, 6, 7]
        m = median(A, B)
        self.assertEqual(4, m)

    def test_ex5(self):
        B = [1, 3, 5]
        A = [7, 9]
        m = median(A, B)
        self.assertEqual(5, m)

    def test_ex6(self):
        A = [1, 3, 8, 9, 15]
        B = [7, 11, 18, 19, 21, 25]
        m = median(A, B)
        self.assertEqual(11, m)

    def test_median_subarray_ex1(self):
        A = [1, 2, 3, 4]
        m = median_of_subarray(SubArray(A, 0, len(A)))
        self.assertEqual(2.5, m)

    def test_median_subarray_ex2(self):
        A = [1, 2, 3, 4, 5]
        m = median_of_subarray(SubArray(A, 0, len(A)))
        self.assertEqual(3, m)

    def test_median_subarray_ex3(self):
        A = [1, 2, 3, 4]
        m = median_of_subarray(SubArray(A, 1, 3))
        self.assertEqual(3, m)

    def test_merge_subarrays(self):
        A = [1, 2, 3]
        B = [4, 5, 6]
        C = merge_subarrays(SubArray(A, 1, 2), SubArray(B, 0, 2))
        self.assertEqual([2, 3, 4, 5], C)

if __name__ == "__main__":
    unittest.main(verbosity=2)