'''
You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
 

Constraints:

1 <= s.length <= 104
s consists of lower-case English letters.
1 <= words.length <= 5000
1 <= words[i].length <= 30
words[i] consists of lower-case English letters.
'''
from typing import List
import unittest
from collections import Counter

# Time Complexity: O(n), Space Complexity: O(n)
def find_substr_with_concat_of_words(s:str, words:List[str])->List[int]:
    if s is None or len(words) < 1 or len(s) < len(words[0]) * len(words):
        return []
    wl = len(words[0])
    cwl = wl * len(words)    
    wt = Counter(words)
    required = len(wt)  
    finds = []
    i = 0    
    for j in range(cwl - 1, len(s)):
        subseq = s[i:j+1]
        state = Counter()
        formed = 0
        for k in range(0, len(subseq), wl):
            w = subseq[k:k+wl]
            state[w] += 1
            if state[w] == wt[w]:
                formed += 1
            if formed == required:
                finds.append(i)    
        i += 1

    return finds

class Tests(unittest.TestCase):
    def test_ex1(self):
        s = "barfoothefoobarman"
        words = ["foo","bar"]
        result = find_substr_with_concat_of_words(s, words)
        self.assertEqual([0, 9], result)

if __name__ == "__main__":
    unittest.main(verbosity = 2)