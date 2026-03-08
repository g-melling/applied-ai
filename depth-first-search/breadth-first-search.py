def dfs(graph, start):
    visited = set()

    def explore(node):
        if node in visited:
            return

        print(node)           # process the node
        visited.add(node)

        for neighbor in graph[node]:
            explore(neighbor)

    explore(start)

if __name__ == "__main__":
    graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

dfs(graph, "A")