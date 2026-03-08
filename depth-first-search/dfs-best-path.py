def find_target(graph, start, target):
    visited = set()

    def explore(node, path):
        # Add current node to the path
        path.append(node)

        print(f"Exploring path: {path} (length: {len(path)})")

        # Check if we found the target
        if node == target:
            print(f"Final path: {path}")
            print(f"Final path length: {len(path)}\n")
            return True

        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if explore(neighbor, path):
                    return True

        # Backtrack: remove the node before returning
        path.pop()
        return False

    return explore(start, [])


if __name__ == "__main__":
    graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

find_target(graph, "A", "C")