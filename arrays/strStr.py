def strStr(haystack: str, needle: str) -> int:
    if needle == "":
        return 0
    m, n = len(haystack), len(needle)
    for i in range(m - n + 1):
        if haystack[i] == needle[0]:
            j = 0
            while j < n:
                if haystack[i + j] != needle[j]:                
                    break
                j += 1
            if j == n:
                return i
    return -1

if __name__ == "__main__":
    # haystack = "hello"
    # needle = "ll"
    haystack = "aaaaa"
    needle = "bba"
    print(strStr(haystack, needle))