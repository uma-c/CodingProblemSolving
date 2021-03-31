'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
   Hide Hint #1  
To reach nth step, what could have been your previous steps? (Think about the step sizes)
'''

def climbStairs(n: int) -> int:
    cache = {}
    def _climbStairs(n: int) -> int:
        if n in cache:
            return cache[n]
        if n < 3:
            return n
        result = _climbStairs(n - 1) + _climbStairs(n - 2)
        cache[n] = result
        return result
    return _climbStairs(n)

def climbStairs1(n: int):
    if n < 3:
        return n
    prev, result = 1, 1
    for i in range(1, n):
        prev, result = result, prev + result
    return result

if __name__ == "__main__":
    print(climbStairs1(5)) # 1 + 1 + 1, 1 + 2, 2 + 1