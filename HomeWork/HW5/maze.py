from collections import deque

def maze_solver_with_teleport(maze: list, portals: dict):
    path = []
    possible_moves = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for index_row, row in enumerate(maze):
        for index_col, col in enumerate(row):
            if col == 'S':
                start = (index_row, index_col)
            if col == 'E':
                end = (index_row, index_col)
                possible_moves.append((index_row, index_col))
            if col == 'P':
                possible_moves.append((index_row, index_col))
            if col == '.':
                possible_moves.append((index_row, index_col))
    count = 0
    while count < 3:
        posible_directions = []
        for direction in directions:
            if (start[0] + direction[0], start[1] + direction[1]) in possible_moves:
                posible_directions.append((start[0] + direction[0], start[1] + direction[1]))
        print(f"the current position: {start}")        # print the current position
        print(f"possible directions: {posible_directions}")         
        if len(posible_directions) == 1:    # if there is only one possible direction
            start = posible_directions[0]   # step to possible direction
            path.append(start)              # add the step to the path

        print(f"the new position: {start}")        # print the current position                       
        print(f"Path: {path}")                        # print the path
        count += 1
    # print(possible_moves)
    pass

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

    maze_solver_with_teleport(maze, portals)
    # distance, path = maze_solver_with_teleport(maze, portals)
    # print(f"Distance: {distance}, Path: {path}")
    # # Output: Distance: 5, Path: [(0, 0), (0, 1), (0, 2), (0, 3), (2, 0), (2, 1), (2, 2), (2, 3)]


    # # Example 2
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
