from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    if strs:
        result = []
        i = 0
        while i < len(strs[0]):
            c = strs[0][i]
            for s in strs:
                if i >= len(s) or s[i] != c:                    
                    return ''.join(result)
            result.append(c)
            i += 1
        return ''.join(result)
    return ''

if __name__ == "__main__":
    #strs = ["flower","flow","flight"]
    strs = ["dog","racecar","car"]
    print(longestCommonPrefix(strs))