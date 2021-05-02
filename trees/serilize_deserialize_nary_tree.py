class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Codec:
    def serialize(self, root: 'Node') -> str:
        def _serialize(node: 'Node'):
            if node:
                result.append(str(node.val))
                if node.children:
                    result.append(':')
                    result.append(str(len(node.children)))
                    result.append('(')
                    children = node.children
                    for i in range(len(node.children) - 1):
                        _serialize(children[i])
                        result.append(',')
                    _serialize(children[-1])
                    result.append(')')
        result = []
        _serialize(root)
        return ''.join(result)

    def deserialize(self, data: str) -> 'Node':
        def _deserialize(s: str) -> 'Node':
            if len(s) > 0:
                s_parts = s.split(':', 1)
                root = Node(int(s_parts[0]))
                if len(s_parts) > 1:
                    children = []
                    ch = s_parts[1]
                    ch_start = ch.index('(')
                    n = int(ch[:ch_start])
                    children_txt = ch[ch_start + 1:len(ch) - 1]
                    children_parts = children_txt.rsplit(',', n - 1)
                    for part in children_parts:
                        children.append(_deserialize(part))
                    root.children = children
                return root
        return _deserialize(data)


if __name__ == "__main__":
    # root = Node(1, [])
    # root.children.append(Node(2))
    # root.children.append(Node(3))
    # root.children.append(Node(4))
    codec = Codec()
    # print(codec.serialize(root))
    s = '1:3(2:3(5,6:1(8),7),3,4)'
    node = codec.deserialize(s)
    print(node)