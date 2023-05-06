class Graph:
    def DFS(self, graph, start):
        visited = set()
        self._dfs_helper(graph, start, visited)
        return visited

    def _dfs_helper(self, graph, start, visited):
        visited.add(start)
        for next_vertex in graph[start] - visited:
            self._dfs_helper(graph, next_vertex, visited)

    def BFS(self, graph, start):
        visited = set()
        queue = [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                queue.extend(graph[vertex] - visited)
        return visited


if __name__ == "__main__":
    g = Graph()
    my_graph = {
        "A": set(["B", "C"]),
        "B": set(["A", "D", "E"]),
        "C": set(["A", "F"]),
        "D": set(["B"]),
        "E": set(["B", "F"]),
        "F": set(["C", "E"]),
    }
    print(g.DFS(my_graph, "B"))
    print(g.BFS(my_graph, "E"))
