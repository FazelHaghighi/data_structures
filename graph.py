class graph:
    def DFS(self, graph, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        for next in graph[start] - visited:
            self.DFS(graph, next, visited)
        return visited

    def BFS(self, graph, start):
        visited, queue = set(), [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                queue.extend(graph[vertex] - visited)
        return visited


if __name__ == "__main__":
    g = graph()
    graph = {
        "A": set(["B", "C"]),
        "B": set(["A", "D", "E"]),
        "C": set(["A", "F"]),
        "D": set(["B"]),
        "E": set(["B", "F"]),
        "F": set(["C", "E"]),
    }
    print(g.DFS(graph, "B"))

    print(g.BFS(graph, "E"))
