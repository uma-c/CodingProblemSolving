'''
875. Koko Eating Bananas
Medium

Koko loves to eat bananas.  There are N piles of bananas, the i-th pile has piles[i] bananas.  The guards have gone and will come back in H hours.

Koko can decide her bananas-per-hour eating speed of K.  Each hour, she chooses some pile of bananas, and eats K bananas from that pile.  If the pile has less than K bananas, she eats all of them instead, and won't eat any more bananas during this hour.

Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.

Return the minimum integer K such that she can eat all the bananas within H hours.

 

Example 1:

Input: piles = [3,6,7,11], H = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], H = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], H = 6
Output: 23
 

Constraints:

1 <= piles.length <= 10^4
piles.length <= H <= 10^9
1 <= piles[i] <= 10^9
'''
from typing import List

'''
Min. eating speed = 1
Max. eating speed = max(piles)
Binary Search towards left to arrive at min. eating spped to finish all pile with in H hours
'''
def can_finish(piles:List[int], H:int, K:int) -> bool:
    req = 0
    for pile in piles:
        req += -(pile // -K) # ceiling division
        if req > H:
            return False
    return req <= H

def min_eating_speed(piles:List[int], H:int) -> int:
    l = 1
    r = max(piles)
    while l <= r:
        m = l + ((r - l) >> 1)
        if can_finish(piles, H, m):
            r = m - 1
        else:
            l = m + 1
    return l

if __name__ == "__main__":
    piles = [3,6,7,11]
    H = 8
    print(min_eating_speed(piles, H))