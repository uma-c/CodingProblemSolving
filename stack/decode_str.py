'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
 

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
'''
'''
3[a2[c]d]ef
'''
def decodeString(s: str) -> str:
    ord_0, ord_9 = ord('0'), ord('9')
    stack = []
    for c in s:
        if c != ']':
            stack.append(c)
        else:
            j = len(stack) - 1
            while j >= 0 and stack[j] != '[':
                j -= 1
            ss = ''.join(stack[j+1:])
            k = j
            j -= 1
            while j >= 0 and len(stack[j]) == 1 and ord_0 <= ord(stack[j]) <= ord_9:
                j -= 1
            t = int(''.join(stack[j+1:k]))
            stack = stack[:j+1]
            stack.append(''.join([ss] * t))
    return ''.join(stack)

if __name__ == "__main__":
    #print(decodeString('3[a2[c]]'))
    #s = "abc3[cd]xyz"
    s = '3[a]2[bc]'
    print(decodeString(s))