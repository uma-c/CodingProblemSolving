class ListNode(object):
    def __init__(self, key, value, prev, next):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class DoubleList(object):
    def __init__(self):
        self._head = None
        self._tail = None

    def addAsFirst(self):
        pass

    def removeLast(self):
        pass

    def remove(node:ListNode):
        pass

    def size(self):
        pass

class LRUCache(object):
    def __init__(self, capacity: int):
        self._hash_map = dict()
        self._list = DoubleList()
        self._capacity = capacity
        self._count = 0

    def contains_key(self, key) -> bool:
        return self.hash_map.get(key) is not None

    def get(self, key):
        return self.hash_map.get(key)

    def put(self, key, value):
        val = self.hash_map.get(key)
        ...
