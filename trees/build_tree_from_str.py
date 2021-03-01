'''
1(4(5)(6))(2(3))

            1
    4                 2
5       6           3

2()(3)
    2
        3
'''
import unittest

class TreeNode(object):
    def __init__(self, key) -> None:
        super().__init__()
        self._key = key
        self._children = []
    
    def get_key(self):
        return self._key

    def get_children(self):
        return tuple(self._children)

    def add_child(self, node):
        self._children.append(node)

def get_node(val):
    if val is None or len(val) < 1:
        return None
    value = int("".join(val))
    return TreeNode(value)

def encode_tree(node):
    if node is None:
        return ""
    
    s = [str(node.get_key())]
    for child in node.get_children():
        s.append("(")
        s.append(encode_tree(child))
        s.append(")")
    return "".join(s)

# Time complexity: O(n), Space complexity: O(n)
def build_tree(s: str)->TreeNode:
    if s is None:
        return s
    
    val = []
    i, lvl = 0, 0
    lvl_nodes_map = dict()
    while i < len(s):
        if s[i] == "(":
            if len(val) > 0:
                node = get_node(val)
                if lvl_nodes_map.get(lvl) is None:
                    lvl_nodes_map[lvl] = []
                lvl_nodes_map[lvl].append(node)
                if lvl > 0:
                    lvl_nodes_map[lvl - 1][-1].add_child(node)
                val = []
            lvl += 1
        elif s[i] == ")":
            lvl -= 1
            if s[i - 1] != ')':
                node = get_node(val)
                lvl_nodes_map[lvl][-1].add_child(node)
                val = []
        else:
            val.append(s[i])
        i += 1

    return lvl_nodes_map[0][0] if lvl_nodes_map.get(0) else None

class Tests(unittest.TestCase):
    def test_ex1(self):
        s = "2()(3)"
        root = build_tree(s)
        self.assertEqual(encode_tree(root), s)

    def test_ex2(self):
        s = "1(4(5)(6))(2(3))"
        root = build_tree(s)
        self.assertEqual(encode_tree(root), s)

    def test_ex3(self):
        s = "1(2)(3)(4)"
        root = build_tree(s)
        self.assertEqual(encode_tree(root), s)

    def test_ex4(self):
        s = "1(2)"
        root = build_tree(s)
        self.assertEqual(encode_tree(root), s)

if __name__ == "__main__":
    unittest.main(verbosity = 2)