class UnionFind:
    def __init__(self, n):
        self._parent = [i for i in range(n+1)]
        self._size = [1] * (n+1)
        self._count = n

    def _root(self, p:int) -> int:
        while self._parent[p] != p:
            self._parent[p] = self._parent[self._parent[p]] # Path compression
            p = self._parent[p]
        return p

    def union(self, p:int, q:int):
        pRoot = self._root(p)
        qRoot = self._root(q)
        if pRoot == qRoot:
            return
        if self._size[pRoot] < self._size[qRoot]:
            self._parent[pRoot] = qRoot
            self._size[qRoot] += self._size[pRoot]
        else:
            self._parent[qRoot] = pRoot
            self._size[pRoot] += self._size[qRoot]
        self._count -= 1

    def connected(self, p:int, q:int) -> bool:
        pRoot = self._root(p)
        qRoot = self._root(q)
        return pRoot == qRoot

    def count(self) -> int:
        return self._count

