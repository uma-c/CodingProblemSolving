'''
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false
 

Constraints:

1 <= n <= 2**31 - 1
'''
def sum_of_sq_of_digits(n : int) -> int:
    result = 0
    while n != 0:
        d = n % 10
        result += d * d
        n //= 10
    return result

def isHappy(n: int) -> bool:
    s = set()
    while n != 1:
        sd = sum_of_sq_of_digits(n)
        if sd in s:
            return False
        s.add(sd)
        n = sd
    return True

if __name__ == "__main__":
    print(isHappy(2))