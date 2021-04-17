import math

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._bucket_capacity = 997
        self._capacity = 10 ** 6
        self._no_of_buckets = math.ceil(self._capacity / self._bucket_capacity)
        self._buckets = [Node(None) for _ in range(self._no_of_buckets)]

    def add(self, key: int) -> None:
        bucket = self._buckets[key % self._bucket_capacity]
        node = bucket
        prev = None
        while node:
            if node.val == key:
                return
            prev, node = node, node.next
        prev.next = Node(key)              

    def remove(self, key: int) -> None:
        bucket = self._buckets[key % self._bucket_capacity]
        node = bucket
        while node.next and node.next.val != key:
            node = node.next
        if node.next and node.next.val == key:
            temp = node.next
            node.next = temp.next
            temp.next = None

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        bucket = self._buckets[key % self._bucket_capacity]
        node = bucket
        while node:
            if node.val == key:
                return True
            node = node.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

if __name__ == "__main__":
    hs = MyHashSet()
    hs.add(1)
    hs.add(2)