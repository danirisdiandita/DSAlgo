from collections import defaultdict, deque


class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        q = deque([])
        q.append(s)
        visited = {}
        visited[s] = True
        prev = []

        while len(q) > 0:
            node = q.popleft()
            neighbors = self.graph[node]

            prev.append(node)

            for neigh in neighbors:
                if visited.get(neigh, False) == False:
                    q.append(neigh)
                    visited[neigh] = True
        return prev


if __name__ == "__main__":
    graph = Graph()
    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(1, 2)
    graph.addEdge(2, 0)
    graph.addEdge(2, 3)
    graph.addEdge(3, 3)
    # print(graph.graph)

    # print(type(graph))

    print(graph.BFS(2))
