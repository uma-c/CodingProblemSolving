'''
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

Example 1:


Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    def merge(list1: ListNode, list2: ListNode, ml: ListNode):
        if not list1 and not list2:
            ml.next = None
            return
        if list1 and list2:
            if list1.val <= list2.val:
                ml.next = list1
                list1 = list1.next
            else:
                ml.next = list2             
                list2 = list2.next            
        elif list1:
            ml.next = list1
            list1 = list1.next
        elif list2:
            ml.next = list2
            list2 = list2.next
        ml = ml.next
        merge(list1, list2, ml)
    mergedList = h = ListNode()
    merge(l1, l2, mergedList)
    return h.next
