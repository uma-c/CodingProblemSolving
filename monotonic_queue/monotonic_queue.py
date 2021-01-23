import collections

class Queue(object):
    def __init__(self):
        self._deque = collections.deque() # decreasing queue; front is max, back is min

    def max(self) -> int:
        return self._deque[0]

    def push(self, val: int):
        while len(self._deque) > 0 and self._deque[-1] < val:
            self._deque.pop()
        self._deque.append(val)

    def pop(self, val: int):
        if len(self._deque) > 0 and self._deque[0] == val:
            self._deque.popleft()