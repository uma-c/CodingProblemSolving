import collections

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self._q = collections.deque()
        self._sum = 0
        self._window_sz = size

    def next(self, val: int) -> float:
        if len(self._q) == self._window_sz:
            self._sum -= self._q.popleft()
        self._q.append(val)
        self._sum += val
        return self._sum / len(self._q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)