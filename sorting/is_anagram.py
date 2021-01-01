import unittest

# O(nlogn)
def is_anagram1(str1: str, str2: str) -> bool:
    if not str1 or not str2:
        raise ValueError('invalid inputs')
    sorted_str1 = ''.join(sorted(list(str1.lower())))
    sorted_str2 = ''.join(sorted(list(str2.lower())))
    return sorted_str1 == sorted_str2

def to_lower(c):
    if 65 <= ord(c) <= 90:
        return chr(ord(c) + 32)
    else:
        return c

# O(n)
def is_anagram(str1: str, str2: str) -> bool:
    if not str1 or not str2:
        raise ValueError('invalid inputs')
    char_map = dict()
    for c in str1:
        lc = to_lower(c)
        if lc in char_map:
            char_map[lc] += 1
        else:
            char_map[lc] = 1
    
    for c in str2:
        lc = to_lower(c)
        if lc in char_map:
            char_map[lc] -= 1
        else:
            return False
        
        if char_map[lc] == 0:
            char_map.pop(lc)

    return len(char_map) == 0

class Tests(unittest.TestCase):
    def test_valid_anagrams1(self):
        self.assertTrue(is_anagram("Army", "Mary"))
    
    def test_valid_anagrams2(self):
        self.assertTrue(is_anagram("Cinema", "Iceman"))

    def test_not_anagrams1(self):
        self.assertFalse(is_anagram("Arm", "Mary"))

    def test_not_anagrams_None1(self):
        with self.assertRaises(ValueError):
            is_anagram(None, "Mary")

    def test_not_anagrams_None2(self):
        with self.assertRaises(ValueError):
            is_anagram("None", None)

    def test_not_anagrams_None3(self):
        with self.assertRaises(ValueError):
            is_anagram(None, None)

if __name__ == "__main__":
    #print(to_lower('h'))
    unittest.main(verbosity=2)