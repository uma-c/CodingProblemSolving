'''
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
'''
from list_node import ListNode

def reverse_linked_list(head:ListNode, m:int, n:int) -> ListNode:
    c = 1
    dummy = ListNode(None, head)
    l_tail = dummy    
    while c < m:
        l_tail = l_tail.next
        c += 1
    i_head = l_tail.next
    prev = i_head
    curr = prev.next
    while c < n:
        temp = curr.next
        curr.next = prev
        prev, curr = curr, temp
        c += 1
    i_head.next = curr
    l_tail.next = prev            
    return dummy.next

if __name__ == "__main__":
    # l = reverse_linked_list(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2, 4)
    # print(l)

    l = reverse_linked_list(ListNode(3, ListNode(5)), 1, 2)
    print(l)