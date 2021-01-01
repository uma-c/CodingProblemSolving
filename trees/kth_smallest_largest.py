import unittest

class TreeNode:
    def __init__(self, val: int, left = None, right = None):
        self.value = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.counter = 0

    def inorder_traversal(self, root:TreeNode):
        if not root:
            return

        self.inorder_traversal(root.left)
        
        self.counter += 1
        print(self.counter, root.value)

        self.inorder_traversal(root.right)

    def find_kth_smallest(self, root: TreeNode, k: int) -> TreeNode:
        if not root:
            return root

        left = self.find_kth_smallest(root.left, k)
        if left:
            return left

        self.counter += 1
        if k == self.counter:
            return root

        return self.find_kth_smallest(root.right, k)

def find_kth_smallest(root: TreeNode, k: int) -> TreeNode:
    curr = root
    stack = []
    while curr or len(stack) > 0:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr
            curr = curr.right

    return None

def find_kth_largest(root: TreeNode, k: int) -> TreeNode:
    curr = root
    stack = []
    while curr or len(stack) > 0:
        if curr:
            stack.append(curr)
            curr = curr.right
        else:
            k -= 1
            curr = stack.pop()
            if k == 0:
                return curr
            curr = curr.left

    return None


class Tests(unittest.TestCase):
    def setUp(self):
        self.root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(7, TreeNode(6), TreeNode(8, None, TreeNode(9))))
    
    def test_ex1(self):
        #inorder_traversal(root)
        #s = Solution()
        #result = s.find_kth_smallest(self.root, 4)
        result = find_kth_smallest(self.root, 4)
        self.assertEqual(4, result.value)

    def test_ex2(self):
        result = find_kth_largest(self.root, 2)
        self.assertEqual(8, result.value)

    def test_ex3(self):
        result = find_kth_largest(self.root, 10)
        self.assertEqual(None, result)

if __name__ == "__main__":
    unittest.main(verbosity=2)