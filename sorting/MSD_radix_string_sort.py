from typing import List
import unittest

def _MSD_radix_string_sort(strs:List[str], i: int) -> List[str]:
    if strs is None or len(strs) < 1:
        return strs
    buckets = [[] for _ in range(26)]
    done_bucket = []
    for string in strs:
        if i < len(string):
            buckets[ord(string[i]) - ord('a')].append(string)
        else:
            done_bucket.append(string)

    sorted_buckets = []
    for bucket in buckets:
        sorted_buckets += _MSD_radix_string_sort(bucket, i + 1)

    return done_bucket + sorted_buckets

def MSD_radix_string_sort(strs:List[str]) -> List[str]:
    return _MSD_radix_string_sort(strs, 0)

class Tests(unittest.TestCase):
    def test_ex1(self):
        nums = ["apple", "banana", "pear", "apricot", "peach", "berry", "ap"]
        result = MSD_radix_string_sort(nums)
        self.assertEqual(["ap", "apple",  "apricot", "banana", "berry", "peach", "pear"], result)

if __name__ == "__main__":
    unittest.main(verbosity = 2)