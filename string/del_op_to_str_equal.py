'''
583. Delete Operation for Two Strings
Medium
Given two words text1 and text2, find the minimum number of steps required to make text1 and text2 the same, where in each step you can delete one character in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Note:
The length of given words won't exceed 500.
Characters in given words can only be lower-case letters.
'''

'''
1143 Medium
'''
def longest_common_subsequence(text1: str, text2: str) -> int:
    if len(text2) < len(text1):
        text1, text2 = text2, text1
    prev = [0 for _ in range(len(text1) + 1)]
    for c1 in text2:
        curr = [0 for _ in range(len(text1) + 1)]
        for j, c2 in enumerate(text1):
            if c1 == c2:
                curr[j + 1] = prev[j] + 1
            else:
                curr[j + 1] = max(curr[j], prev[j + 1])
        prev = curr
    return prev[-1]

def min_ops_to_make_strs_equal(text1:str, text2:str) -> int:
    lcs = longest_common_subsequence(text1, text2)
    return len(text1) + len(text2) - (lcs << 1)

if __name__ == "__main__":
    # w1 = "abcba"
    # w2 = "abcbcba"
    w1 = "dinitrophenylhydrazine"
    w2 = "dimethylhydrazine"
    print(min_ops_to_make_strs_equal(w1, w2))