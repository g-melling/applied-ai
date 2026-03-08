def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            print(node)
            visited.add(node)

            # Add neighbors in reverse so leftmost is visited first
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

if __name__ == "__main__":
    graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

dfs_iterative(graph, "A")