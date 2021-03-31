# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode) -> ListNode:
    '''
    1 -> 2 -> 3 -> 4 -> 5
    '''
    if head and head.next:
        new_head = reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head
    else:
        return head