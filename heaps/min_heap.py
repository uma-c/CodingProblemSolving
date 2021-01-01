import unittest

class MinHeap(object):
    def __init__(self):
        self._array = []

    def __len__(self):
        return len(self._array)

    def extract_min(self):
        if not self._array:
            return None
        if len(self._array) == 1:
            return self._array.pop(0)
        # take root and set right-most element as root and bubble down until heap property is satisfied
        min_key = self._array[0]
        self._array[0] = self._array.pop(-1)
        self._bubble_down(0)
        return min_key

    def insert(self, key):
        if key is None:
            raise ValueError("key cannot be None")
        # add as last element and bubble up
        self._array.append(key)
        self._bubble_up(len(self._array) - 1)

    def peek_min(self):
        return self._array[0] if self._array else None

    def _bubble_up(self, index):
        if index == 0:
            return
        parent = (index - 1) // 2
        if self._array[index] < self._array[parent]:
            self._array[parent], self._array[index] = self._array[index], self._array[parent]
            self._bubble_up(parent)

    def _bubble_down(self, index):
        smaller_child_index = self._find_smaller_child_index(index)
        if smaller_child_index == -1:
            return
        if self._array[index] > self._array[smaller_child_index]:
            self._array[index], self._array[smaller_child_index] = self._array[smaller_child_index], self._array[index]
            self._bubble_up(smaller_child_index)

    def _find_smaller_child_index(self, index):
        left_child_index = index * 2 + 1
        right_child_index = index * 2 + 2
        if right_child_index < len(self._array): # left and right exist
            if self._array[index] > self._array[left_child_index] or self._array[index] > self._array[right_child_index]:
                return left_child_index if self._array[left_child_index] < self._array[right_child_index] else right_child_index
            else:
                return -1
        else: # right does not exist
            if left_child_index < len(self._array): # left exist
                return left_child_index if self._array[left_child_index] < self._array[index] else -1
            else:
                return -1

class Tests(unittest.TestCase):
    def test_peek_min(self):
        heap = MinHeap()
        self.assertEqual(None, heap.peek_min())

    def test_extract_min(self):
        heap = MinHeap()
        self.assertEqual(None, heap.extract_min())

    def test_insert(self):
        heap = MinHeap()
        items = [5, 3, 4, 2, 7]
        for item in items:
            heap.insert(item)
        self.assertEqual(min(items), heap.peek_min())

    def test_extract(self):
        heap = MinHeap()
        items = [5, 3, 4, 2, 7]
        for item in items:
            heap.insert(item)
        self.assertEqual(2, heap.extract_min())
        self.assertEqual(3, heap.extract_min())
        heap.insert(1)
        self.assertEqual(1, heap.extract_min())

    def test_len(self):
        heap = MinHeap()
        items = [5, 3, 4, 2, 7]
        for item in items:
            heap.insert(item)
        self.assertEqual(5, len(heap))
        heap.extract_min()
        self.assertEqual(4, len(heap))

if __name__ == "__main__":
    unittest.main(verbosity=2)        