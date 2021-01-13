'''
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
'''
from list_node import ListNode

def remove_dups(head:ListNode) -> ListNode:
    dummy = ListNode(None)
    result = dummy
    node = head    
    while node:
        c = 0
        curr = node.next        
        while curr and node.val == curr.val:
            c += 1
            curr = curr.next
        if c == 0:
            node.next = None
            result.next = node            
            result = result.next
        node = curr
    return dummy.next

if __name__ == "__main__":
    l = remove_dups(ListNode(1,ListNode(2,ListNode(3,ListNode(3,ListNode(4,ListNode(4,ListNode(5))))))))
    print(l)