class Heap:
    def get_parent(k):
        return (k - 1) // 2

    def __init__(self, comparator):
        self.arr = []
        self.comparator = comparator    

    def peek(self):
        return self.arr[0]

    def push(self, v):
        self.arr.append(v)
        self._heapify_up(len(self.arr) - 1)

    def pop(self):
        self.arr[0] = self.arr[-1]
        self.arr.pop()
        self._heapify_down(0)

    def _heapify_up(self, k):
        parent = Heap.get_parent(k)
        if parent == -1:
            return
        if not self.comparator(self.arr[parent], self.arr[k]):
            self.arr[parent], self.arr[k] = self.arr[k], self.arr[parent]
            self._heapify_up(parent)

    def _heapify_down(self, k):
        if k >= len(self.arr):
            return
        left = 2 * k + 1
        right = 2 * k + 2
        index = k
        if left < len(self.arr) and not self.comparator(self.arr[index], self.arr[left]):
            index = left
        if right < len(self.arr) and not self.comparator(self.arr[index], self.arr[right]):
            index = right
        if index != k:
            self.arr[index], self.arr[k] = self.arr[k], self.arr[index]
            self._heapify_down(index)

    def make_heap(self, arr):
        for _, v in enumerate(arr):
            self.arr.append(v)

        index = (len(self.arr) - 1) // 2
        for i in range(index, -1, -1):
            self._heapify_down(i)


if __name__ == "__main__":
    min_heap = Heap(lambda a, b : a < b)
    max_heap = Heap(lambda a, b : a > b)

    arr = [4, 3, 5, 2, 1, 6, 8, 7, 9]
    min_heap.make_heap(arr)
    max_heap.make_heap(arr)

    print(min_heap.peek())
    print(max_heap.peek())

    min_heap.push(0)
    max_heap.push(10)

    print(min_heap.peek())
    print(max_heap.peek())

    min_heap.pop()
    max_heap.pop()

    print(min_heap.peek())
    print(max_heap.peek())