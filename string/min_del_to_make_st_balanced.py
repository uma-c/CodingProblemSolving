'''
1653. Minimum Deletions to Make String Balanced
Medium
You are given a string s consisting only of characters 'a' and 'b'​​​​.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.

 

Example 1:

Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").
Example 2:

Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.
 

Constraints:

1 <= s.length <= 105
s[i] is 'a' or 'b'​​.
'''

def lis(s:str):
    if not s:
        return 0
    subseq = [s[0]]
    for i in range(1, len(s)):
        if ord(s[i]) >= ord(subseq[-1]):
            subseq.append(s[i])
        else:
            l, r = 0, len(subseq) - 1
            while l <= r:
                m = l + ((r - l) >> 1)
                if ord(s[i]) < ord(subseq[m]):                    
                    r = m - 1
                else:
                    l = m + 1
            if 0 <= l < len(subseq):
                subseq[l] = s[i]
    return len(subseq)

def min_deletions(s:str) -> int:
    a, res = 0, 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == 'a':
            a += 1
        elif s[i] == 'b':
            if a > 0:
                a -= 1
                res += 1
    return res

if __name__ == "__main__":
    print(min_deletions('bbaaaaabb'))
