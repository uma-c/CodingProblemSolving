'''
Given a linked list, swap every two adjacent nodes and return its head.
 

Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]
 

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
 

Follow up: Can you solve the problem without modifying the values in the list's nodes? (i.e., Only nodes themselves may be changed.)
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head: ListNode) -> ListNode:
    '''
    1 -> 2 -> 3
    Sub-problems: 1 -> 2, 3
    2 -> 1, 3
    2 -> 1 -> 3
    '''
    if head and head.next:
        temp = head.next.next
        n0 = head
        n1 = head.next
        n1.next = n0
        n0.next = swapPairs(temp)
        return n1
    else:
        return head
