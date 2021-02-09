class Node:
    def __init__(self):
        self.children = dict()

class Trie:
    def __init__(self):
        self._root = Node()

    def insert(self, s:str):
        node = self._root
        for c in s:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
                