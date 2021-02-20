class ListNode:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._tail = ListNode()
        self._head = ListNode(next=self._tail)
        self._tail.prev = self._head

    def _get(self, index: int) -> int:
        """
        Get the node of the index-th node in the linked list. If the index is invalid, return -1.
        """
        i = 0
        node = self._head.next
        while i < index and node:
            node = node.next
            i += 1
        return node

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        node = self._get(index)
        return node.val if node and node != self._tail else -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = ListNode(val, self._head, self._head.next)
        self._head.next.prev = new_node
        self._head.next = new_node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = ListNode(val, self._tail.prev, self._tail)
        self._tail.prev.next = new_node
        self._tail.prev = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        node = self._get(index)
        if not node:
            return
        new_node = ListNode(val, node.prev, node)
        node.prev.next = new_node
        node.prev = new_node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        node = self._get(index)
        if not node or node == self._tail:
            return
        temp1 = node.prev
        temp2 = node.next
        node.prev = None
        node.next = None
        temp1.next = temp2
        temp2.prev = temp1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)