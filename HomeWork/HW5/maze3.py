from collections import deque


def maze_solver_with_teleport(maze: list, portals: dict):
    block_loop_portals = []
    possible_moves = []
    path = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for index_row, row in enumerate(maze):
        for index_col, col in enumerate(row):
            if col in ['P', '.']:
                possible_moves.append((index_row, index_col))
            elif col == 'S':
                start = (index_row, index_col)
                path.append(start)
            elif col == 'E':
                end = (index_row, index_col)
                possible_moves.append((index_row, index_col))
    print(f"Possible Moves: {possible_moves}")

    count = 0
    while count < 100:
        possible_directions = []
        if start in portals and start not in block_loop_portals:
            print("Teleporting")
            start = portals[start]
            path.append(start)
        for direction in directions:
            direction_check = start[0] + direction[0], start[1] + direction[1]
            if direction_check in possible_moves and direction_check not in path:
                possible_directions.append(direction_check)
        print(f"Current Position: {start}")
        print(f"Possible Directions: {possible_directions}")
        print(f"Path: {path}")
        print(count)
        print()
        if len(possible_directions) == 1:
            start = possible_directions[0]
            path.append(start)
        elif len(possible_directions) == 0 and start in portals:
            start = portals[start]
            block_loop_portals.append(start)
            path.append(start)
        else:
            break
        
        if start == end:
            print("End Reached")
            print(f"Path: {path}")
            break
        count += 1


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

    # distance, path = maze_solver_with_teleport(maze, portals)
    # print(f"Distance: {distance}, Path: {path}")
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

    maze_solver_with_teleport(maze, portals)
    # distance, path = maze_solver_with_teleport(maze, portals)
    # print(f"Distance: {distance}, Path: {path}")
    # # Expected Output: Distance: 6, Path: [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (0, 5), (1, 5), (2, 5)]
