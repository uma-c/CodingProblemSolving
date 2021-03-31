from typing import List

def _reverseString(s: List[str], left: int, right: int) -> None:
    if left < right:
        s[left], s[right] = s[right], s[left]
        _reverseString(s, left + 1, right - 1)

def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    _reverseString(s, 0, len(s) - 1)

if __name__ == "__main__":
    s = ['h', 'e', 'l', 'l', 'o']
    reverseString(s)
    print(s)