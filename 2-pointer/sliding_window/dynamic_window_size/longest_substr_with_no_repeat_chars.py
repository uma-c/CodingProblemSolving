import unittest

'''
if less than 2 chars, return input string
set state to first char
set max_len is 1
set left to 0, right to 1
loop until right hits last char
    if char is not in state
        add to state
    else
        loop until left hits repeated char
            remove left char from state
        move left beyond repeated char by 1
    record state
'''
def longest_substr_no_repeat_chars(s:str)->str:   
    if not s or len(s) < 2:
        return s

    max_i, max_j = 0, 0
    i, j = 0, 1
    state = {s[i]}
    while j < len(s):
        if not s[j] in state:
            state.add(s[j])
        else:
            while s[i] != s[j]: # until repeated char is removed
                state.remove(s[i])                
                i += 1
            i += 1 # move next beyond repeated character 
        if (j - i) > (max_j - max_i):
            max_j, max_i = j, i
        j += 1
    print(max_i, max_j)
    return s[max_i:(max_j + 1)]

class Tests(unittest.TestCase):
    def test_example1(self):
        result = longest_substr_no_repeat_chars("abcabcbb")
        self.assertEqual(result, "abc")

    def test_example2(self):
        result = longest_substr_no_repeat_chars("bbbbbbb")
        self.assertEqual(result, "b")

    def test_example3(self):
        result = longest_substr_no_repeat_chars("abcd")
        self.assertEqual(result, "abcd")

if __name__ == "__main__":
    unittest.main(verbosity=2)