class MyCircularQueue:

    def __init__(self, k: int):
        self._arr = [None] * k
        self._start = 0
        self._count = 0

    def enQueue(self, value: int) -> bool:
        if self._count < len(self._arr):
            end = (self._start + self._count) % len(self._arr)
            self._arr[end] = value
            self._count += 1
            return True
        
        return False

    def deQueue(self) -> bool:
        if self._count > 0:
            self._start = (self._start + 1) % len(self._arr)
            self._count -= 1
            return True
        return False

    def Front(self) -> int:
        if self._count > 0:
            return self._arr[self._start]
        return -1

    def Rear(self) -> int:
        if self._count > 0:
            return self._arr[(self._start + self._count  - 1) % len(self._arr)]
        return -1

    def isEmpty(self) -> bool:
        return self._count == 0

    def isFull(self) -> bool:
        return self._count == len(self._arr)


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()