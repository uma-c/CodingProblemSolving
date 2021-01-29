'''
460. LFU Cache
Hard
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

 

Example 1:

Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[3,4], cnt(4)=2, cnt(3)=3
 

Constraints:

0 <= capacity, key, value <= 104
At most 105 calls will be made to get and put.
 

Follow up: Could you do both operations in O(1) time complexity?
'''

class DoublyLinkedListNode:
    def __init__(self, key, value, prev=None, next=None, freq_node=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next
        self.freq_node = freq_node

class DoubleList:
    def __init__(self):
        self._head = DoublyLinkedListNode(None, None)
        self._tail = DoublyLinkedListNode(None, None, self._head)
        self._head.next = self._tail
        self._size = 0

    def size(self):
        return self._size

    def add_first(self, node):
        temp = self._head.next
        self._head.next = node
        temp.prev = node
        node.next = temp
        node.prev = self._head
        self._size += 1

    def remove(self, node):
        next = node.next
        prev = node.prev
        node.next = None
        node.prev = None
        prev.next = next
        next.prev = prev
        self._size -= 1

    def remove_last(self):
        if self._tail.prev != self._head:
            node = self._tail.prev
            self.remove(node)
            return node
        return None

class FreqCounterNode:
    def __init__(self, freq, prev=None, next=None):
        self.freq = freq
        self.prev = prev
        self.next = next
        self.double_list = DoubleList()

class OrderedFreqDoubleList:
    def __init__(self):
        self._head = FreqCounterNode(None, None)
        self._tail = FreqCounterNode(None, None, self._head)
        self._head.next = self._tail    

    def add_after(self, node, new_node):
        temp = node.next
        node.next = new_node
        temp.prev = new_node
        new_node.next = temp
        new_node.prev = node

    def add_first(self, node):
        self.add_after(self._head, node)

    def on_access(self, node):
        freq_node = node.freq_node
        if freq_node:
            freq_node.double_list.remove(node)        
            freq = freq_node.freq
            new_freq_node = None
            if freq_node.next and freq_node.next.freq == (freq + 1):
                new_freq_node = freq_node.next
            else:
                new_freq_node = FreqCounterNode(freq + 1)
                self.add_after(freq_node, new_freq_node)
            node.freq_node = new_freq_node
            new_freq_node.double_list.add_first(node)           
            if freq_node.double_list.size() == 0:
                self.remove(freq_node)            
        else:
            freq = 1
            if self._head.next != self._tail and self._head.next.freq == freq:
                freq_node = self._head.next             
            else:
                freq_node = FreqCounterNode(freq)                
                self.add_first(freq_node)
            node.freq_node = freq_node
            freq_node.double_list.add_first(node)

    def remove(self, freq_node):
        next = freq_node.next
        prev = freq_node.prev
        freq_node.next = None
        freq_node.prev = None
        prev.next = next
        next.prev = prev        

    def remove_lfu(self):
        if self._head.next != self._tail:
            node = self._head.next.double_list.remove_last()
            if self._head.next.double_list.size() == 0:
                self.remove(self._head.next)
            return node
        return None

class LFUCache:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._hashmap = dict()
        self._freq_list = OrderedFreqDoubleList()

    def get(self, key: int) -> int:
        if key in self._hashmap:
            node = self._hashmap[key]
            self._freq_list.on_access(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self._hashmap:
            node = self._hashmap[key]
            node.value = value            
        else:
            if len(self._hashmap) == self._capacity:
                removed_node = self._freq_list.remove_lfu()
                if removed_node:
                    self._hashmap.pop(removed_node.key)
            if not (len(self._hashmap) < self._capacity):
                return           
            node = DoublyLinkedListNode(key, value)
            self._hashmap[key] = node 
        self._freq_list.on_access(node)

if __name__ == "__main__":
    # lfuc = LFUCache(2)
    # lfuc.put(1, 1)
    # lfuc.put(2, 2)
    # print(lfuc.get(1))
    # lfuc.put(3, 3)
    # print(lfuc.get(2))
    # print(lfuc.get(3))
    # lfuc.put(4, 4)
    # print(lfuc.get(1))
    # print(lfuc.get(3))
    # print(lfuc.get(4))
    lfuc = LFUCache(0)
    lfuc.put(0, 0)
    print(lfuc.get(0))