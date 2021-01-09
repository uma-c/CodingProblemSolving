import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        node1 = self
        node2 = other
        while node1 is not None and node2 is not None and node1.val == node2.val:
            node1 = node1.next
            node2 = node2.next

        return node1 is None and node2 is None

def merge(head1:ListNode, head2:ListNode):
    merge_head = ListNode()
    head_sentinel = merge_head
    node1, node2 = head1, head2
    while node1 is not None and node2 is not None:
        if node2.val < node1.val:
            merge_head.next = node2            
            node2 = node2.next
        else:
            merge_head.next = node1
            node1 = node1.next
        merge_head = merge_head.next

    if node1 is not None:
        merge_head.next = node1
        merge_head = merge_head.next

    if node2 is not None:
        merge_head.next = node2
        merge_head = merge_head.next
    return head_sentinel.next

def sort_list(head:ListNode) -> ListNode:
    if head is None or head.next is None:
        return head
    slow, fast = head, head.next
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    h2 = slow.next
    slow.next = None
    head1 = sort_list(head)
    head2 = sort_list(h2)
    return merge(head1, head2)

class Tests(unittest.TestCase):
    def test_ex1(self):
        head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
        sorted_list_head = sort_list(head)
        self.assertTrue(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))) == sorted_list_head)

if __name__ == "__main__":
    unittest.main(verbosity = 2)