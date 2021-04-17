import math

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._bucket_capacity = 997
        self._capacity = 10 ** 6
        self._no_of_buckets = math.ceil(self._capacity / self._bucket_capacity)
        self._buckets = [Node(None) for _ in range(self._no_of_buckets)]        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        bucket = self._buckets[key % self._bucket_capacity]
        node = bucket
        prev = None
        while node:
            if node.val and node.val[0] == key:
                node.val = (key, value)
                return
            prev, node = node, node.next
        prev.next = Node((key, value))    

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        bucket = self._buckets[key % self._bucket_capacity]
        node = bucket
        while node:
            if node.val and node.val[0] == key:
                return node.val[1]
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        bucket = self._buckets[key % self._bucket_capacity]
        node = bucket
        while node.next and node.next.val and node.next.val[0] != key:
            node = node.next
        if node.next and node.next.val and node.next.val[0] == key:
            temp = node.next
            node.next = temp.next
            temp.next = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)