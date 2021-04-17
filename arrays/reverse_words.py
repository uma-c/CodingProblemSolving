'''
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
Example 4:

Input: s = "  Bob    Loves  Alice   "
Output: "Alice Loves Bob"
Example 5:

Input: s = "Alice does not even like bob"
Output: "bob like even not does Alice"
 

Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.
 

Follow up: Could you solve it in-place with O(1) extra space?
'''

from typing import List

def reverseWords(s: str) -> str:
    def reverse(sl:List[str], start: int, end: int):
        while start < end:
            sl[start], sl[end] = sl[end], sl[start]
            start += 1
            end -= 1
    if len(s) > 0:
        s1 = []
        j = 0
        while s[j] == ' ':
            j += 1
        for i in range(j, len(s) - 1):
            if s[i] == ' ' and s[i] == s[i + 1]:
                continue
            s1.append(s[i])
        if s[-1] != ' ':
            s1.append(s[-1])        
        reverse(s1, 0, len(s1) - 1)
        i = 0
        for j in range(len(s1)):
            if s1[j] == ' ':
                reverse(s1, i, j - 1)
                i = j + 1
        reverse(s1, i, len(s1) - 1)
        return ''.join(s1)
    return s

if __name__ == "__main__":
    #s = "  Bob    Loves  Alice   "
    s = "  hello world  "
    print(reverseWords(s), end='|')
