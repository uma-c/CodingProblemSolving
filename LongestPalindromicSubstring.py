def preProcess(s:str) -> str:
    if len(s) > 0:
        return '#' + str.join('#', s) + '#'
    else:
        return s
    
def longestPalindrome(s: str) -> str:
    if len(s) < 1:
        return ''

    n = len(s)
    p = [0] * n
    c = 0
    r = 0
    for i in range(1, n, 1):
        iMirror = 2*c - i # i's mirror
        if r > i:
            p[i] = min(r-i, p[iMirror])
        else:
            p[i] = 0
        
        while i + 1 + p[i] < n and s[i + 1 + p[i]] == s[i - 1 - p[i]]:
            p[i] += 1

        if i + p[i] > r: # range expanded and center is updated
            r = p[i] + i
            c = i
    
    r, c = max(p), p.index(max(p))
    return s[(c-r) : (c+r)].replace('#', '')

class Solution:
    def longestPalindrome(self, s: str) -> str:
        return longestPalindrome(preProcess(s))
        

if __name__ == '__main__':
    sol = Solution()
    palindrome = sol.longestPalindrome('banana')
    print(palindrome)
