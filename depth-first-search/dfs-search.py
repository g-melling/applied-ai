def find_target(graph, start, target):
    visited = set()

    def explore(node, path):
        
        visited.add(node)
        path.append(node)

        if node == target:
            print(f"Final path = {path}")
            print(f"Path length = {len(path)}")
            return True

        for neighbor in graph[node]:
            if neighbor not in visited:
                if explore(neighbor, path):
                    return True

        # backtrack
        # path.pop()
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


"""
def find_all_and_best_paths(graph, start, target):
    all_paths = []
    visited = set()

    def explore(node, path):
        visited.add(node)
        path.append(node)

        # If target is reached, record the path
        if node == target:
            print(f"Found path: {path} (length: {len(path)})")
            all_paths.append(path.copy())
        else:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    explore(neighbor, path)

        # Backtrack
        path.pop()
        visited.remove(node)

    explore(start, [])

    # Find the shortest path
    best_path = min(all_paths, key=len) if all_paths else None

    return all_paths, best_path
"""