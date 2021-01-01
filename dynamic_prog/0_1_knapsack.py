import unittest
from typing import List, Tuple

# Time complexity - O(nw), Space complexity i.e. O(w)  n - no. of items, w - capacity
def get_max_value_knapsack(wv: Tuple[Tuple[int]], capacity: int) -> int:
    if not wv or len(wv) < 1:
        return 0

    n = len(wv)
    prev_row = [0] * (capacity + 1)
    curr_row = None
    for i in range(1, n+1):
        curr_row = [0] * (capacity + 1)
        for w in range(1, capacity + 1):
            if w < wv[i - 1][0]:
                curr_row[w] = prev_row[w]
            else:
                curr_row[w] = max(wv[i - 1][1] + prev_row[w - wv[i - 1][0]], prev_row[w])
        #print(curr_row)
        prev_row = curr_row
    return 0 if not curr_row else curr_row[capacity]

def _get_max_val_knapsack_recursive(wv: Tuple[Tuple[int]], capacity: int, i: int) -> int:
    if i == len(wv) or capacity <= 0:
        return 0

    without_i = _get_max_val_knapsack_recursive(wv, capacity, i+1)
    with_i = 0
    if wv[i][0] <= capacity:
        with_i = wv[i][1] + _get_max_val_knapsack_recursive(wv, capacity - wv[i][0], i+1)

    return max(with_i, without_i)

def get_max_val_knapsack_recursive(wv: Tuple[Tuple[int]], capacity: int) -> int:
    return _get_max_val_knapsack_recursive(wv, capacity, 0)

def _get_max_val_knapsack_top_down(wv: Tuple[Tuple[int]], capacity: int, i: int, cache: List[List[int]]) -> int:
    if i == len(wv) or capacity <= 0:
        return 0

    if cache[i][capacity] is None:
        without_i = _get_max_val_knapsack_top_down(wv, capacity, i+1, cache)
        with_i = 0
        if wv[i][0] <= capacity:
            with_i = wv[i][1] + _get_max_val_knapsack_top_down(wv, capacity - wv[i][0], i+1, cache)
        cache[i][capacity] = max(with_i, without_i)
    return cache[i][capacity]

def get_max_val_knapsack_top_down(wv: Tuple[Tuple[int]], capacity: int) -> int:
    cache = [[None for _ in range(capacity + 1)] for _ in range(len(wv) + 1)]
    return _get_max_val_knapsack_top_down(wv, capacity, 0, cache)

class Tests(unittest.TestCase):
    def test_example1(self):
        wv = ((1, 1), (3, 4), (4, 5), (5, 7))
        max_value = get_max_value_knapsack(wv, 7)
        self.assertEqual(max_value, 9)

    def test_example_no_items(self):
        wv = ()
        max_value = get_max_value_knapsack(wv, 7)
        self.assertEqual(max_value, 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)