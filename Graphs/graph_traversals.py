import unittest
from typing import List, Dict, Set

class Graph(object):
    def __init__(self, n: int, adj_list:Dict[int, Set[int]]):
        self._n = n
        self.adj_list = adj_list

    def size(self)->int:
        return self._n

    def dfs(self, start_vertex)->List[int]:
        visited = [False] * (self._n + 1)
        path = []
        self._dfs(start_vertex, visited, path)
        return path

    def get_connected_components(self)->List[List[int]]:
        visited = [False] * (self._n + 1)
        components = []
        for vertex in range(1, self._n + 1):
            if not visited[vertex]:
                path = []
                self._dfs(vertex, visited, path)
                components.append(path)

        return components

    def _dfs(self, vertex: int, visited:List[int], path: List[int])->None:
        if visited[vertex]:
            return
        
        visited[vertex] = True
        path.append(vertex)
        neighbours = self._adj_list.get(vertex)
        if neighbours is not None:
            for neighbour in neighbours:
                self._dfs(neighbour, visited, path)

    def bfs(self, start_vertex, end_vertex = None)->List[int]:
        visited = [False] * (self._n + 1)
        path = []
        queue = [start_vertex]
        vertex = start_vertex
        while len(queue) > 0 and vertex != end_vertex:
            vertex = queue.pop(0)
            if not visited[vertex]:
                visited[vertex] = True
                path.append(vertex)
                neighbours = self._adj_list.get(vertex)
                if neighbours is not None:
                    for neighbour in neighbours:
                        queue.append(neighbour)
        return path

    def shortest_path(self, start_vertex: int, end_vertex: int)->List[int]:
        if start_vertex is None or end_vertex is None:
            raise ValueError("invalid input")
        visited = [False] * (self._n + 1)
        visited[start_vertex] = True
        prev = [None] * (self._n + 1)
        queue = [start_vertex]
        vertex = start_vertex
        found = False
        while len(queue) > 0 and not found:
            vertex = queue.pop(0)
            neighbours = self._adj_list.get(vertex)
            if neighbours is not None:
                for neighbour in neighbours:
                    if not visited[neighbour]:
                        visited[neighbour] = True
                        prev[neighbour] = vertex
                        if neighbour != end_vertex:
                            queue.append(neighbour)
                        else:
                            found = True
                            break
        if found:                       
            shortest_path = []
            at = end_vertex
            while at is not None:
                shortest_path.append(at)
                at = prev[at]
            shortest_path.reverse()
            return shortest_path
        return []

class Tests(unittest.TestCase):
    def setUp(self):
        adj_list = dict()# adjacency list
        adj_list[1] = {2, 3}
        adj_list[2] = {4}
        adj_list[3] = {4}
        adj_list[4] = {5}
        adj_list[5] = {6, 7, 8}
        self.graph =  Graph(9, adj_list)

    def test_dfs(self):        
        path = self.graph.dfs(1)
        self.assertEqual([1, 2, 4, 5, 8, 6, 7, 3], path)

    def test_bfs(self):        
        path = self.graph.bfs(1)
        self.assertEqual([1, 2, 3, 4, 5, 8, 6, 7], path)

    def test_connected_components(self):        
        connected_components = self.graph.get_connected_components()
        self.assertEqual([[1, 2, 4, 5, 8, 6, 7, 3], [9]], connected_components)

    def test_shortest_path(self):
        adj_list = dict()# adjacency list
        adj_list[1] = {2, 3}
        adj_list[2] = {1, 6}
        adj_list[3] = {4, 5}
        adj_list[4] = {3, 9}
        adj_list[5] = {3, 7}
        adj_list[6] = {2, 7}
        adj_list[7] = {5, 6, 8}
        adj_list[8] = {7, 9}
        adj_list[9] = {4, 8}
        graph =  Graph(9, adj_list)
        shortest_path = graph.shortest_path(1, 7)
        self.assertEqual([1, 2, 6, 7], shortest_path)

if __name__ == "__main__":
    unittest.main(verbosity=2)