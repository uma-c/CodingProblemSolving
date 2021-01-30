'''
72. Edit Distance
Hard

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 

Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
'''

def min_edit_distance1(word1:str, word2:str) -> int:
    memo = [[None for _ in range(len(word2))] for _ in range(len(word1))]   
    def dp(i, j):
        if i < 0:
            return j + 1
        
        if j < 0:
            return i + 1

        if memo[i][j]:
            return memo[i][j]

        if word1[i] == word2[j]:
            memo[i][j] = dp(i - 1, j - 1)
        else:
            memo[i][j] = min(dp(i - 1, j - 1) + 1, dp(i, j - 1) + 1, dp(i - 1, j) + 1) # replace, insert, delete
        return memo[i][j]

    return dp(len(word1) - 1, len(word2) - 1)

def min_edit_distance(word1:str, word2:str) -> int:
    if len(word1) < len(word2):
        word1, word2 = word2, word1
    
    prev = [i for i in range(len(word2)+1)]
    for i in range(1, len(word1)+1):
        row = [i for _ in range(len(word2)+1)]
        for j in range(1, len(word2) + 1):
            if word1[i - 1] == word2[j - 1]:
                row[j] = prev[j - 1]
            else:
                row[j] = min(row[j - 1] + 1, min(prev[j - 1] + 1, prev[j] + 1))
        prev = row
    return prev[-1]

if __name__ == "__main__":
    print(min_edit_distance('horse', 'ros'))
    print(min_edit_distance('intention', 'execution'))
    print(min_edit_distance('plasma', 'altruism'))