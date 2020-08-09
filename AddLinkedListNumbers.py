class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry_over = 0
        result = ListNode()
        prev = result
        while l1 != None and l2 != None:            
            sum_of_digits = l1.val + l2.val + carry_over
            sum_digit_node = ListNode()
            if sum_of_digits < 10:
                sum_digit_node.val = sum_of_digits
                carry_over = 0
            else:
                sum_digit_node.val = sum_of_digits - 10
                carry_over = 1
            prev.next = sum_digit_node
            prev = sum_digit_node
            l1 = l1.next
            l2 = l2.next

        while l1 != None:
            sum_of_digits = l1.val + carry_over
            sum_digit_node = ListNode()
            if sum_of_digits < 10:
                sum_digit_node.val = sum_of_digits
                carry_over = 0
            else:
                sum_digit_node.val = sum_of_digits - 10
                carry_over = 1
            prev.next = sum_digit_node
            prev = sum_digit_node
            l1 = l1.next

        while l2 != None:
            sum_of_digits = l2.val + carry_over
            sum_digit_node = ListNode()
            if sum_of_digits < 10:
                sum_digit_node.val = sum_of_digits
                carry_over = 0
            else:
                sum_digit_node.val = sum_of_digits - 10
                carry_over = 1
            prev.next = sum_digit_node
            prev = sum_digit_node
            l2 = l2.next

        if carry_over == 1:
            prev.next = ListNode(1)

        return result.next

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# 1024 + 548 = 1572
# (4 -> 2 -> 0 -> 1) + (8 -> 4 -> 5)
if __name__ == '__main__':
    #num1 = ListNode(2, ListNode(4, ListNode(3)))
    #num2 = ListNode(5, ListNode(6, ListNode(4)))
    num1 = ListNode(4, ListNode(2, ListNode(0, ListNode(1))))
    num2 = ListNode(8, ListNode(4, ListNode(5)))
    sol = Solution()
    result_node = sol.addTwoNumbers(num1, num2)
    while result_node != None:
        print(result_node.val, end=' -> ')
        result_node = result_node.next