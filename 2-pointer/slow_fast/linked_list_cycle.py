'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null
'''
import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        cycle = False
        while fast and fast.next:            
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                cycle = True
                break

        if cycle:
            slow = head
            while fast and slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
        return None

if __name__ == '__main__':
    unittest.main(verbosity=2)        