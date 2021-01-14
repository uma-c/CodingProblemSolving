'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
'''
from list_node import ListNode
from reverse_list import reverse_list

def reorder_list(head:ListNode) -> None:
    if not head:
        return head
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    right = slow.next
    slow.next = None    
    l1 = head
    l2 = reverse_list(right)     
    while l1 and l2:
        temp1 = l1.next
        temp2 = l2.next
        l1.next = l2
        l2.next = temp1
        l1 = temp1
        l2 = temp2

if __name__ == "__main__":
    h = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7)))))))
    reorder_list(h)
    print(h)