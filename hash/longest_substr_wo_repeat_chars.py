def lengthOfLongestSubstring(s: str) -> int:
    if not s or len(s) < 1:
        return 0

    result = 0
    i = j = 0
    state = set()
    for j in range(len(s)):
        if not s[j] in state:
            state.add(s[j])
        else:
            while s[i] != s[j]: # until repeated char is removed
                state.remove(s[i])                
                i += 1
            i += 1 # move next beyond repeated character 
        result = max(result, j - i + 1)
    return result

if __name__ == "__main__":
    print(lengthOfLongestSubstring('abcabcbb'))