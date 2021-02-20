from list_node import ListNode

def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    node = headA
    l1 = 0
    while node:
        l1 += 1
        node = node.next
    node = headB
    l2 = 0
    while node:
        l2 += 1
        node = node.next
    short = long = None
    if l1 <= l2:
        short = headA
        long = headB
    else:
        short = headB
        long = headA
    dl = abs(l1 - l2)
    while dl > 0 and long:
        dl -= 1
        long = long.next
    while short and long:
        if short == long:
            return short
        short = short.next
        long = long.next
    return None