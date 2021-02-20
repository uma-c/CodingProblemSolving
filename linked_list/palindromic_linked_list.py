from list_node import ListNode
from reverse_list import reverse_list

def isPalindrome(head: ListNode) -> bool:
    '''
    1 -> 2 -> 2 -> 1
    l = 1 -> 2
    r = 1 -> 2
    True

    1 -> 2 -> 1
    l = 1 -> 2
    r = 1
    True
    '''
    if not head:
        return True
    slow = head
    fast = head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    if prev:
        prev.next = None
    l = head
    r = reverse_list(slow)
    while l and r:
        if l.val != r.val:
            return False
        l = l.next
        r = r.next
    if (r and r.next) or (l and l.next):
        return False
    return True

if __name__ == "__main__":
    print(isPalindrome(ListNode(0, ListNode(0))))