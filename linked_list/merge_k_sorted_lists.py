'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.
'''
from typing import List
from list_node import ListNode
import heapq
import queue

class ListNodeProxy:
    def __init__(self, l:ListNode):
        self.l = l
    def __lt__(self, other):
        return self.l.val < other.l.val
    def __eq__(self, other):
        return self.l.val == other.l.val

def merge1(lists: List[ListNode]) -> ListNode:
    if lists is None or len(lists) < 1:
        return None
    q = queue.SimpleQueue()
    sentinel = ListNode(None)
    result = sentinel
    nodes = []
    for l in lists:
        if l:
            nodes.append(l)
    if nodes:
        q.put(nodes)
    h = []
    while not q.empty():
        n = []
        for node in q.get():
            temp = node.next
            node.next = None
            heapq.heappush(h, ListNodeProxy(node))
            if temp:
                n.append(temp)
        result.next = heapq.heappop(h).l
        result = result.next
        if n:
            q.put(n)
    while len(h) > 0:
        result.next = heapq.heappop(h).l
        result = result.next
    return sentinel.next

def merge2lists(l1:ListNode, l2:ListNode) -> ListNode:
    if l1 is None:
        return l2
    
    if l2 is None:
        return l1

    sentinel = result = ListNode(None)
    while l1 and l2:
        if l1.val < l2.val:
            temp = l1.next
            l1.next = None
            result.next = l1
            l1 = temp
        else:
            temp = l2.next
            l2.next = None
            result.next = l2
            l2 = temp
        result = result.next
    if l1:
        result.next = l1
    if l2:
        result.next = l2
    return sentinel.next

'''
Divide and Conquer approach
Time complexity: O(n log k), Space complexity: O(1)
'''
def merge(lists: List[ListNode]) -> ListNode:
    if len(lists) > 2:
        m = len(lists) // 2
        l1 = merge(lists[0:(m + 1)])
        l2 = merge(lists[(m+1):])
        return merge2lists(l1, l2)
    elif len(lists) == 2:
        return merge2lists(lists[0], lists[1])
    elif len(lists) == 1:
        return lists[0]
    return None

if __name__ == "__main__":
    h = merge([ListNode(1,ListNode(4,ListNode(5))),ListNode(1,ListNode(3,ListNode(4))),ListNode(2,ListNode(6))])
    print(h)
    