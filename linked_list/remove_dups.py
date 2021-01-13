'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
'''
from list_node import ListNode

def remove_duplicates(head:ListNode) -> ListNode:
    if head is None:
        return head
    prev = head
    curr = head.next
    while curr is not None:
        if prev.val == curr.val:
            prev.next = curr.next
            curr.next = None
            curr = prev.next
        else:
            prev = curr
            curr = curr.next
    return head