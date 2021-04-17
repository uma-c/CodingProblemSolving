'''
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "God Ding"
Output: "doG gniD"
 

Constraints:

1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
'''
from typing import List

def reverseWords(s: str) -> str:
    def reverse(start: int, end: int):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
    s = list(s)    
    result = []
    i = 0
    for j in range(len(s)):
        if s[j] == ' ':
            reverse(i, j - 1)
            i = j + 1
    reverse(i, len(s) - 1)
    return ''.join(s)

def reverseWords(s: str) -> str:
    w = s.split()
    w = [e[::-1] for e in w]
    return ' '.join(w)

if __name__ == "__main__":
    #s = "Let's take LeetCode contest"
    s = "God Ding"
    print(reverseWords(s))