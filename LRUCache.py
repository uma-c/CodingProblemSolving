'''
146. LRU Cache
Medium

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
Follow up:
Could you do get and put in O(1) time complexity?

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 3000
0 <= value <= 104
At most 3 * 104 calls will be made to get and put.
'''

class DoublyLinkedListNode:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class DoubleList:
    def __init__(self):
        self._head = DoublyLinkedListNode(None, None) # sentinel
        self._tail = DoublyLinkedListNode(None, None) # sentinel
        self._head.next = self._tail
        self._tail.prev = self._head

    def add_first(self, node):
        temp = self._head.next 
        self._head.next = node
        node.prev = self._head
        node.next = temp
        temp.prev = node

    def remove(self, node):
        if node:
            temp = node.next                
            node.next = None
            node.prev.next = temp
            temp.prev = node.prev
            node.prev = None

    def remove_last(self):
        node = self._tail.prev
        if node != self._head:
            self.remove(node)
            return node

        return None

class LRUCache:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._hashmap = dict()
        self._double_list = DoubleList()

    def get(self, key: int) -> int:
        if key in self._hashmap:
            node = self._hashmap[key]
            self._double_list.remove(node)
            self._double_list.add_first(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self._hashmap:
            self._hashmap[key].val = value
            self.get(key)
        else:
            if self._capacity == len(self._hashmap):
                last = self._double_list.remove_last()
                self._hashmap.pop(last.key)
            node = DoublyLinkedListNode(key, value)
            self._double_list.add_first(node)
            self._hashmap[key] = node

if __name__ == "__main__":
    # lruc = LRUCache(2)
    # lruc.put(2, 1)
    # lruc.put(1, 1)
    # lruc.put(2, 3)
    # lruc.put(4, 1)
    # print(lruc.get(1))
    # print(lruc.get(2))

    lruc = LRUCache(1)
    lruc.put(2, 1)
    print(lruc.get(2))
