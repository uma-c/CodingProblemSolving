from list_node import ListNode

def rotateRight(head: ListNode, k: int) -> ListNode:
    if not head or not k:
        return head
    l, node = 1, head
    while node.next:
        l += 1
        node = node.next
    k = k % l
    node.next = head
    node = head
    for _ in range(l - k - 1):
        node = node.next
    ans = node.next
    node.next = None
    return ans
        