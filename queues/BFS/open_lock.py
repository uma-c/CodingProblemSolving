from typing import List
import collections

def openLock(deadends: List[str], target: str) -> int:
    def neighbors(node):
        for i in range(4):
            x = int(node[i])
            for d in (-1, 1):
                y = (x + d) % 10
                yield node[:i] + str(y) + node[i+1:]
    deadend_set = set(deadends)
    visited = {'0000'}
    q = collections.deque([('0000', 0)])
    while len(q) > 0:
        node, depth = q.popleft()
        if node == target:
            return depth
        if node in deadend_set:
            continue
        for nb in neighbors(node):
            if nb not in visited:
                visited.add(nb)
                q.append((nb, depth + 1))
    return -1

if __name__ == "__main__":
    deadends = ["0201","0101","0102","1212","2002"]
    target = "0202"
    print(openLock(deadends, target))