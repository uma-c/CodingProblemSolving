'''
524. Longest Word in Dictionary through Deleting
Medium
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output: 
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output: 
"a"
Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.
'''
from typing import List, Dict

def contains(s:str, w:str) -> bool:
    if len(w) > len(s):
        return False
    j = 0
    for c in s:
        if j < len(w):
            if c == w[j]:
                j += 1
        else:
            break
    return j == len(w)

def find_longest_word(s: str, d: List[str]) -> str:
    d.sort()
    max_wl, long_w = float("-inf"), ""
    for w in d:
        if contains(s, w):
            if len(w) > max_wl:
                max_wl = len(w)
                long_w = w
    return long_w

if __name__ == "__main__":
    s = "abpcplea"
    d = ["ale","apple","monkey","plea"]
    print(find_longest_word(s, d))