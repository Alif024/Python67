from collections import deque


def maze_solver_with_teleport(maze: list, portals: dict):
    # Direction vectors for moving up, down, left, and right
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Find the start ('S') and end ('E') positions in the maze
    start = end = None
    rows, cols = len(maze), len(maze[0])
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start = (r, c)
            elif maze[r][c] == 'E':
                end = (r, c)

    # BFS setup
    queue = deque([(start, 0, [])])  # (position, distance, path)
    visited = set([start])

    # BFS loop
    while queue:
        (r, c), distance, path = queue.popleft()
        print(f"Queue: {queue}")
        print(f"Visited: {visited}")

        # If we've reached the end, return the distance and path
        if (r, c) == end:
            print("End reached")
            return distance, path + [(r, c)]
        print()

        # Explore the 4 adjacent cells
        for dr, dc in directions:
            print(f"Direction [dr: {dr}, dc: {dc}]")
            nr, nc = r + dr, c + dc
            print(f"New Position [nr: {nr}, nc: {nc}]")
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != '#' and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append(((nr, nc), distance + 1, path + [(r, c)]))
                print(f"Queue: {queue}")
                print(f"Visited: {visited}")
            print()

        # Check for portal teleportation
        if (r, c) in portals:
            portal_exit = portals[(r, c)]
            print(f"Portal Exit: {portal_exit}, r: {r}, c: {c}")
            if portal_exit not in visited:
                visited.add(portal_exit)
                queue.append((portal_exit, distance + 1, path + [(r, c)]))
                print(f"Queue: {queue} [{(nr,nc)}, {distance + 1}, {path + [(r, c)]}]")
                print(f"Visited: {visited}")
        print()
        print()

    # If no path is found, return -1 for distance and an empty path
    print("No path found")
    return -1, []


if __name__ == "__main__":
    # Example 1
    maze = [
        ['S', '.', '.', 'P'],
        ['#', '#', '.', '#'],
        ['P', '.', '.', 'E'],
        ['#', '#', '#', '#']
    ]

    portals = {
        (0, 3): (2, 0),  # Portal from (0, 3) to (2, 0)
        (2, 0): (0, 3)   # Portal from (2, 0) to (0, 3)
    }

    distance, path = maze_solver_with_teleport(maze, portals)
    print(f"Distance: {distance}, Path: {path}")
    # Output: Distance: 5, Path: [(0, 0), (0, 1), (0, 2), (0, 3), (2, 0), (2, 1), (2, 2), (2, 3)]

    # Example 2
    # maze = [
    #     ['S', '.', '#', 'P', '#', 'P'],
    #     ['#', '.', '#', '.', '#', '.'],
    #     ['#', '.', 'P', '.', '.', 'E'],
    #     ['P', '#', '#', '#', '#', '#'],
    #     ['#', '.', '.', 'P', '.', '.']
    # ]

    # portals = {
    #     (0, 3): (3, 0),  # Portal from (0, 3) to (3, 0)
    #     (3, 0): (0, 3),  # Portal from (3, 0) to (0, 3)
    #     (0, 5): (2, 2),  # Portal from (0, 5) to (2, 2)
    #     (2, 2): (0, 5)   # Portal from (2, 2) to (0, 5)
    # }

    # distance, path = maze_solver_with_teleport(maze, portals)
    # print(f"Distance: {distance}, Path: {path}")
    # # Expected Output: Distance: 6, Path: [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (0, 5), (1, 5), (2, 5)]
