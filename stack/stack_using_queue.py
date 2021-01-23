import queue

class Stack(object):
    def __init__(self):
        self._q = queue.Queue()
        self._top = None

    def push(self, val:int):
        self._q.put(val)
        self._top = val

    def pop(self) -> int:
        size = self._q.qsize()
        while size > 2:
            self._q.put(self._q.get())
            size -= 1
        self._top = self._q.get()
        self._q.put(self._top)
        return self._q.get()

    def top(self) -> int:
        return self._top

    def empty(self) -> bool:
        return self._q.empty()

if __name__ == "__main__":
    s = Stack()
    s.push(3)
    s.push(2)
    s.push(1)
    print(s.top())
    print(s.pop())
    print(s.pop())
    print(s.empty())
    print(s.pop())
    print(s.empty())