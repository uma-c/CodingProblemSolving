from typing import List, Set
from collections import Counter
import unittest

'''
[1, 3, 5]
0 items - 3c0 = 1
1 item - 3c1 = 3
2 items - 3c2 = 3
3 items - 3c3 = 1
all combinations = 8 = 2^3
'''
def _combinations_recursive(A:Set[int])->List[Set[int]]:
    if len(A) < 1:
        return [set()]

    num = A.pop()
    perms = _combinations_recursive(A)
    for i in range(len(perms)):
        perm = perms[i].copy()
        perm.add(num)
        perms.append(perm)
    return perms

def combinations_recursive(A:Set[int])->List[Set[int]]:
    return _combinations_recursive(A)

def combinations(nums:List[int])->List[List[int]]:
    result = [[]]
    num_map = Counter(nums)
    for num in num_map.keys():
        start = len(result)
        for j in range(len(result)):
            subset = result[j].copy()             
            subset.append(num)            
            result.append(subset)
             
        for _ in range(1, num_map[num]):                            
            end = len(result)
            for k in range(start, end):
                subset = result[k].copy()
                subset.append(num)
                result.append(subset)
            start = end  
    return result

class Tests(unittest.TestCase):
    def test_ex1(self):
        A = [1, 3, 5]
        result = combinations(A)
        expected = [[], [1], [3], [1, 3], [5], [1, 5], [3, 5], [1, 3, 5]]
        self.assertEqual(expected, result)

    def test_ex2(self):
        A = [1, 2, 2, 2]
        result = combinations(A)
        expected = [[], [1], [2], [1, 2], [2, 2], [1, 2, 2], [2, 2, 2], [1, 2, 2, 2]]
        self.assertEqual(expected, result)
    
    def test_ex3(self):
        result = combinations("aba")
        expected = [[], ['a'], ['a', 'a'], ['b'], ['a', 'b'], ['a', 'a', 'b']]
        self.assertEqual(expected, result)

    def test_ex4(self):
        result = combinations("aaa")
        expected = [[], ['a'], ['a', 'a'], ['a', 'a', 'a']]
        self.assertEqual(expected, result)

    def test_ex5(self):
        result = combinations("lee")
        expected = [[], ['l'], ['e'], ['l', 'e'], ['e', 'e'], ['l', 'e', 'e']]
        self.assertEqual(expected, result)

if __name__ == "__main__":
    unittest.main(verbosity = 2)