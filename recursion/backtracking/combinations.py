'''
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Example 2:

Input: n = 1, k = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20
1 <= k <= n
'''

from typing import List

def combine(n: int, k: int) -> List[List[int]]:
    def backtrack(start, combination, result):
        if k == len(combination):
            result.append(combination.copy())
            return

        for i in range(start, n + 1):
            combination.append(i)
            backtrack(i + 1, combination, result)
            combination.pop(-1)
    result = []
    backtrack(1, [], result)
    return result

if __name__ == "__main__":
    print(combine(4, 2))