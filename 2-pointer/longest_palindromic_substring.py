def ps(s:str, l, r) -> int:
    n = len(s)
    while 0 <= l < n and 0 <= r < n and s[l] == s[r]:
        l -= 1
        r += 1
    return r - l - 1

def lps(s:str) -> int:
    if not s or len(s) < 1:
        return 0
    l = 1
    for i in range(1, len(s)):
        l1 = ps(s, i, i)
        l2 = ps(s, i - 1, i)
        l = max(l, l1, l2)
    return l

if __name__ == "__main__":
    print(lps('cbbd'))
    #print(lps('a'))