'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''
from list_node import ListNode

def add_numbers(l1:ListNode, l2:ListNode) -> ListNode:    
    sum_vals = l1.val + l2.val
    result_head = ListNode(sum_vals % 10)
    carry_over = 0 if sum_vals < 10 else 1
    curr1, curr2 = l1.next, l2.next
    result_curr = result_head
    while curr1 is not None and curr2 is not None:
        sum_vals = carry_over + curr1.val + curr2.val
        carry_over = 0 if sum_vals < 10 else 1
        result_curr.next = ListNode(sum_vals % 10)        
        curr1 = curr1.next
        curr2 = curr2.next
        result_curr = result_curr.next
    while curr1 is not None:
        sum_vals = carry_over + curr1.val
        carry_over = 0 if sum_vals < 10 else 1
        result_curr.next = ListNode(sum_vals % 10)
        curr1 = curr1.next
        result_curr = result_curr.next
    while curr2 is not None:
        sum_vals = carry_over + curr2.val
        carry_over = 0 if sum_vals < 10 else 1
        result_curr.next = ListNode(sum_vals % 10)
        curr2 = curr2.next
        result_curr = result_curr.next
    if carry_over != 0:
        result_curr.next = ListNode(carry_over)
    return result_head
