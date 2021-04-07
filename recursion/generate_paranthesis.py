'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
'''
from typing import List

def generateParenthesis(n: int) -> List[str]:
    def backtrack(open: int, close: int, combination: List[str], result: List[str]):
        if len(combination) == 2 * n:
            result.append(''.join(combination))
            return

        if open < n:
            combination.append("(")
            backtrack(open + 1, close, combination, result)
            combination.pop(-1)

        if close < open:
            combination.append(")")
            backtrack(open, close + 1, combination, result)
            combination.pop(-1)
    result = []
    backtrack(0, 0, [], result)
    return result

if __name__ == "__main__":
    print(generateParenthesis(3))
    
