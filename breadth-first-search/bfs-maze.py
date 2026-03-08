from collections import deque

def bfs_maze(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])

    # Directions: up, down, left, right
    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    queue = deque([start])
    visited = set([start])
    parent = {start: None}

    while queue:
        current = queue.popleft()
        if current == end:
            # Reconstruct path
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            path_length = len(path) - 1
            return path_length, path

        r, c = current
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            neighbor = (nr, nc)
            # Check bounds and if open path
            if 0 <= nr < rows and 0 <= nc < cols:
                if maze[nr][nc] != '#' and neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    queue.append(neighbor)

    return None, None  # No path found

if __name__ == "__main__":
    # Define maze
    maze = [
        ['S', '.', '.', '#'],
        ['.', '#', '.', '.'],
        ['.', '#', '.', 'E']
    ]

    # Find start and end positions
    start = end = None
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == 'S':
                start = (r,c)
            elif maze[r][c] == 'E':
                end = (r,c)

    length, path = bfs_maze(maze, start, end)
    print("Path length:", length)
    print("Shortest path:", path)
