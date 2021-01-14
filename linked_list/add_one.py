'''
MSD is head
e.g.
9->9->9
1->0->0->0
'''

from list_node import ListNode

def _add_one(head:ListNode) -> ListNode:
    if head.next is None:
        head.val += 1
    else:
        new_next = _add_one(head.next)
        if new_next.val > 9:
            new_next.val = 0
            head.val += 1
        head.next = new_next
    return head
def add_one(head:ListNode) -> ListNode:
    if head is None:
        return None
    
    head = _add_one(head)
    if head.val > 9:
        head.val = 0
        return ListNode(1, head)
    return head

if __name__ == "__main__":
    h = add_one(ListNode(9, ListNode(9, ListNode(9))))
    print(h)