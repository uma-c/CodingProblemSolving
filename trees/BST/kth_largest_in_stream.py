from typing import List
import heapq

class TreeNode:
    def __init__(self, val: int, count=1, left=None, right=None):
        self.val = val
        self.count = count
        self.left = left
        self.right = right

    def kthLargest(self, k:int) -> int:
        def _kthLargest(node: TreeNode, k1: int):
            rc = node.right.count if node.right else 0
            lc = node.left.count if node.left else 0
            nc = node.count - rc - lc
            if node.right and rc >= k1:
                return _kthLargest(node.right, k1)
            elif node.left and k1 - rc > nc:
                return _kthLargest(node.left, k1 - rc - nc)
            else:
                return node.val                
        return _kthLargest(self, k)

    def add(self, val: int):
        def _add(node: TreeNode, parent: TreeNode):            
            if node:
                node.count += 1
                if node.val < val:
                    _add(node.right, node)
                elif node.val > val:
                    _add(node.left, node)
            else:
                new_node = TreeNode(val)
                if parent:
                    if parent.val < val:
                        parent.right = new_node
                    else:
                        parent.left = new_node
        _add(self, None)
            
class KthLargestUsingBST:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        if nums:
            self.bst = TreeNode(nums[0])
            for i in range(1, len(nums)):
                self.bst.add(nums[i])
        else:
            self.bst = None            

    def add(self, val: int) -> int:
        if self.bst:
            self.bst.add(val)
        else:
            self.bst = TreeNode(val)
        return self.bst.kthLargest(self.k)

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.k_min_heap = nums
        heapq.heapify(self.k_min_heap)
        while len(nums) > k:
            heapq.heappop(self.k_min_heap)

    def add(self, val: int) -> int:
        if len(self.k_min_heap) < self.k:
            heapq.heappush(self.k_min_heap, val)
        else:
            heapq.heappushpop(self.k_min_heap, val)
        return self.k_min_heap[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

if __name__ == "__main__":
    nums = [4,5,8,2]
    k = 3
    obj = KthLargest(k, nums)
    print(obj.add(3))
    print(obj.add(5))
    print(obj.add(10))
    print(obj.add(9))
    print(obj.add(4))