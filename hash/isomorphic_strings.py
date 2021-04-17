'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
'''

def isIsomorphic(s: str, t: str) -> bool:
    map1 = dict()
    map2 = dict()
    for i in range(len(s)):
        if s[i] in map1:
            if map1[s[i]] != t[i]: # two chars mapped to same char
                return False
        elif t[i] in map2:
            if map2[t[i]] != s[i]:
                return False    
        map1[s[i]] = t[i]
        map2[t[i]] = s[i]
    return True

if __name__ == "__main__":
    print(isIsomorphic('paper', 'title'))