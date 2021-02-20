from list_node import ListNode

def detectCycle(head: ListNode) -> ListNode:
    if not head:
        return None
    slow = fast = head
    has_cycle = False
    while fast and fast.next:        
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break
    if has_cycle:
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
    return None