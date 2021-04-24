'''
Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"
Note:
letters has a length in range [2, 10000].
letters consists of lowercase letters, and contains at least 2 unique letters.
target is a lowercase letter.

Hint#1
Try to find whether each of 26 next letters are in the given string array.
'''

from typing import List

def nextGreatestLetter(letters: List[str], target: str) -> str:
    l, r = 0, len(letters) - 1
    while l <= r:
        m = l + (r - l) // 2
        if letters[m] < target:
            l = m + 1
        else:
            r = m - 1
    return letters[l] if l < len(letters) else letters[0]

if __name__ == "__main__":
    letters = ["c", "f", "j"]#["c", "f", "j"]
    target = "d"
    print(nextGreatestLetter(letters, target))