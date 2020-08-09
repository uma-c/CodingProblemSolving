class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = {}
        result = 0
        index = 0
        substr_start = 0
        for ch in s: 
            ch_last_index = cache.get(ch)           
            if ch_last_index != None and ch_last_index >= substr_start:
                result = max(result, index - substr_start)                
                substr_start = ch_last_index + 1

            cache[ch] = index
            index += 1
        
        result = max(result, index - substr_start)
        return result

if __name__ == '__main__':
    # Input: "abcabcbb"
    # Output: 3 
    # Explanation: The answer is "abc", with the length of 3.

    # Input: "abba"
    # Output: 2 
    # Explanation: The answer is "ab", with the length of 2.    
    sol = Solution()
    print(sol.lengthOfLongestSubstring('abba'))