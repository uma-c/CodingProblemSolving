'''
Given an integer representing a given amount of change, write a
function to compute minimum number of coins required to make
that amount of change. You can assume that there is always a
1¢ coin.
eg. (assuming American coins: 1, 5, 10, and 25 cents)
makeChange(1) = 1 (1)
makeChange(6) = 2 (5 + 1)
makeChange(49) = 7 (25 + 10 + 10 + 1 + 1 + 1 + 1)
'''
import unittest
from typing import Tuple, Dict

def makeChangeDpTopDown(c: int, coins: Tuple[int], cache: Dict[int, int]) -> int:
    if c in cache:
        return cache[c]

    min_coins = float("inf")
    for i in range(len(coins) - 1, -1, -1):
        if c < coins[i]:
            continue
        n = makeChangeDpTopDown(c - coins[i], coins, cache) + 1
        min_coins = min(n, min_coins)

    return min_coins

def makeChange(c: int, coins: Tuple[int]) -> int:
    cache = dict()
    cache[0] = 0
    for coin in coins:
        cache[coin] = 1
    return makeChangeDpTopDown(c, coins, cache)

# bottom up dynamic programming
def makeChange1(c: int, coins: Tuple[int]) -> int:
    cache = dict()
    cache[0] = 0    
    for i in range(1, c + 1):        
        min_coins = float("inf")
        for coin in coins:
            if coin <= i:
                n = cache[i - coin] + 1
                min_coins = min(min_coins, n)
            else:
                break
        cache[i] = min_coins

    print(cache)
    return cache[c]

class Tests(unittest.TestCase):
    def setUp(self):
        self.coins = (1, 5, 10, 25)

    def test_ex1(self):
        result = makeChange1(40, self.coins)
        self.assertEqual(3, result)

    def test_ex2(self):
        result = makeChange1(12, self.coins)
        self.assertEqual(3, result)

if __name__ == "__main__":
    unittest.main(verbosity=2)