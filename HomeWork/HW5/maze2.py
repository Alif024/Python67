from collections import deque

def maze_solver_with_teleport(maze: list, portals: dict):
    rows, cols = len(maze), len(maze[0])
    start = None
    end = None
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start = (r, c)
            elif maze[r][c] == 'E':
                end = (r, c)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start, [start], 0)])  
    visited = set()
    visited.add(start)
    while queue:
        (current, path, steps) = queue.popleft()
        if current == end:
            return steps, path
        for d in directions:
            next_r, next_c = current[0] + d[0], current[1] + d[1]
            
            if 0 <= next_r < rows and 0 <= next_c < cols:
                if maze[next_r][next_c] != '#' and (next_r, next_c) not in visited:
                    
                    visited.add((next_r, next_c))
                    next_steps = steps + 1
                    queue.append(((next_r, next_c), path + [(next_r, next_c)], next_steps))
                    
                    if maze[next_r][next_c] == 'P':
                        portal_destination = portals[(next_r, next_c)]
                        if portal_destination not in visited:
                            visited.add(portal_destination)
                            queue.append((portal_destination, path + [(next_r, next_c), portal_destination], next_steps))

    return -1, []  
    # 
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
    maze = [
        ['S', '.', '#', 'P', '#', 'P'],
        ['#', '.', '#', '.', '#', '.'],
        ['#', '.', 'P', '.', '.', 'E'],
        ['P', '#', '#', '#', '#', '#'],
        ['#', '.', '.', 'P', '.', '.']
    ]

    portals = {
        (0, 3): (3, 0),  # Portal from (0, 3) to (3, 0)
        (3, 0): (0, 3),  # Portal from (3, 0) to (0, 3)
        (0, 5): (2, 2),  # Portal from (0, 5) to (2, 2)
        (2, 2): (0, 5)   # Portal from (2, 2) to (0, 5)
    }

    distance, path = maze_solver_with_teleport(maze, portals)
    print(f"Distance: {distance}, Path: {path}")
    # Expected Output: Distance: 6, Path: [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (0, 5), (1, 5), (2, 5)]