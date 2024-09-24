from collections import deque

def maze_solver_with_teleport(maze: list, portals: dict):
    from random import choice
    all_paths = []
    dead_end = {}
    path = []
    possible_moves = []
    fork_points = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for index_row, row in enumerate(maze):
        for index_col, col in enumerate(row):
            if col == 'S':
                start = (index_row, index_col)
                path.append(start)
            if col == 'E':
                end = (index_row, index_col)
                possible_moves.append((index_row, index_col))
            if col == 'P':
                possible_moves.append((index_row, index_col))
            if col == '.':
                possible_moves.append((index_row, index_col))
    count = 0
    while count < 17:
        posible_directions = []
        for direction in directions:
            # print(f"direction: {start[0] + direction[0], start[1] + direction[1]}")
            direction_check = start[0] + direction[0], start[1] + direction[1]      # if (1,2) in dead_end.values() and start must be (2,2) then it will not append to posible_directions
            check_dead_end = True
            for key, value in dead_end.items():
                if value == direction_check and key == start:
                    check_dead_end = False
            if direction_check in possible_moves and direction_check not in path and check_dead_end:
                posible_directions.append(direction_check)
        if start in portals and portals[start] not in path:
            posible_directions.append(portals[start])
        print(f"the current position: {start}")        # print the current position
        print(f"possible directions: {posible_directions}")         
        if len(posible_directions) == 1:    # if there is only one possible direction
            start = posible_directions[0]   # step to possible direction
            path.append(start)              # add the step to the path
        elif len(posible_directions) == 0:  # if there is no possible direction
            print(f"the new position: {start}")        # print the current position                       
            print(f"Path: {path}")                     # print the path
            print(f"Fork Points: {fork_points}")
            print(f"Dead End: {dead_end}")
            print(f"All Paths: {all_paths}")
            dead_end.clear()
            try:
                dead_end[fork_points[-1][0]] = fork_points[-1][1]
            except:
                break
            start = fork_points[-1][0]      # go back to the fork point
            # reset the path to the fork point
            path = path[:path.index(fork_points[-1][0]) + 1]
            fork_points.pop()
        elif len(posible_directions) > 1:
            rand_direction = choice(posible_directions)
            # if start == (0,2) and (0,3) in posible_directions:
            #     rand_direction = (0,3)
            # elif start == (2,2) and (1,2) in posible_directions:
            #     rand_direction = (1,2)
            # elif start == (2,2) and (2,1) in posible_directions:
            #     rand_direction = (2,1)
            # fork_points[start] = rand_direction
            fork_points.append((start, rand_direction))
            start = rand_direction
            path.append(start)
        print(f"the new position: {start}")        # print the current position                       
        print(f"Path: {path}")                     # print the path
        print(f"Fork Points: {fork_points}")
        print(f"Dead End: {dead_end}")
        # add the path to all paths and reset the path for find new possible path
        if start == end:
            all_paths.append(path)
            print(f"All Paths: {all_paths}")
            dead_end.clear()
            try:
                dead_end[fork_points[-1][0]] = fork_points[-1][1]
            except:
                break
            start = fork_points[-1][0]
            path = path[:path.index(fork_points[-1][0]) + 1]
            fork_points.pop()
        count += 1
        
        print(f"Count: {count}")
        print()
    # print(possible_moves)
    pass

if __name__ == "__main__":
    # Example 1
    # maze = [
    #     ['S', '.', '.', 'P'],
    #     ['#', '#', '.', '#'],
    #     ['P', '.', '.', 'E'],
    #     ['#', '#', '#', '#']
    # ]

    # portals = {
    #     (0, 3): (2, 0),  # Portal from (0, 3) to (2, 0)
    #     (2, 0): (0, 3)   # Portal from (2, 0) to (0, 3)
    # }

    # maze_solver_with_teleport(maze, portals)
    # distance, path = maze_solver_with_teleport(maze, portals)
    # print(f"Distance: {distance}, Path: {path}")
    # # Output: Distance: 5, Path: [(0, 0), (0, 1), (0, 2), (0, 3), (2, 0), (2, 1), (2, 2), (2, 3)]


    # # Example 2
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

    maze_solver_with_teleport(maze, portals)
    # distance, path = maze_solver_with_teleport(maze, portals)
    # print(f"Distance: {distance}, Path: {path}")
    # # Expected Output: Distance: 6, Path: [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (0, 5), (1, 5), (2, 5)]
