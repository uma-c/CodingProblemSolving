from queue import LifoQueue

class QueueWithStacks:
    def __init__(self):
        self._s1 = LifoQueue()
        self._s2 = LifoQueue()

    def empty(self):
        return self._s1.empty() and self._s2.empty()

    def push(self, val:int):
        self._s1.put(val)

    def peek(self):
        last_item = None
        while not self._s1.empty():
            last_item = self._s1.get()
            self._s2.put(last_item)
        if last_item:        
            self._s2.put(last_item)
        return last_item

    def pop(self) -> int:
        self.peek()
        return self._s2.get()    

if __name__ == "__main__":
    s = QueueWithStacks()
    s.push(3)
    s.push(2)
    s.push(1)
    print(s.peek())
    print(s.pop())
    print(s.pop())
    print(s.empty())
    print(s.pop())
    print(s.empty())