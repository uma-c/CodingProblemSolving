'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
'''

from typing import List

def letterCombinations(digits: str) -> List[str]:
    if digits:
        buttons = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z'] ]
        a = buttons[int(digits[0]) - 2]
        b = []
        for d in digits[1:]:
            t = int(d) - 2
            for j in buttons[t]:
                for k in a:
                    b.append(k + j)
            a, b = b, []
        return a
    else:
        return []

if __name__ == "__main__":
    print(letterCombinations('234'))