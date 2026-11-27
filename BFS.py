def bfs(start, goal, rows, columns, obstacles):

    # check if start and goal are within grid boundaries and not blocked by obstacles
    if not (0 <= start[0] <= columns - 1 and 0 <= start[1] <= rows - 1):
        return "Invalid start coordinates"

    if not (0 <= goal[0] <= columns - 1 and 0 <= goal[1] <= rows - 1):
        return "Invalid goal coordinates"

    if start in obstacles:
        return "Start position is blocked by an obstacle"

    if goal in obstacles:
        return "Goal position is blocked by an obstacle"

    queue = [[start]]
    visited = {start}

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node == goal:
            return path

        x, y = node

        neighbors = [
            (x+1, y),
            (x-1, y),
            (x, y+1),
            (x, y-1)
        ]

        for neighbor in neighbors:
            nx, ny = neighbor

            # check for grid boundaries, obstacles, and visited
            if (0 <= nx <= columns - 1 and 0 <= ny <= rows - 1
                    and neighbor not in obstacles
                    and neighbor not in visited):

                visited.add(neighbor)

                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None


rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

start_x, start_y = input("Enter start coordinates (x,y): ").split(",")
goal_x, goal_y = input("Enter goal coordinates (x,y): ").split(",")

start = (int(start_x), int(start_y))
goal = (int(goal_x), int(goal_y))

obstacles = set()

number_of_obstacles = int(input("Enter number of obstacles: "))

for i in range(number_of_obstacles):
    obstacle_x, obstacle_y = input("Enter obstacle coordinates (x,y): ").split(",")
    obstacles.add((int(obstacle_x), int(obstacle_y)))


# special costs
special_costs = {}

number_of_special_nodes = int(input("Enter number of special-cost nodes: "))

for i in range(number_of_special_nodes):

    special_x, special_y = input("Enter special node coordinates (x,y): ").split(",")

    special_cost = int(input("Enter the cost of this node: "))

    special_costs[(int(special_x), int(special_y))] = special_cost


result = bfs(start, goal, rows, columns, obstacles)


if result is None:
    print("No path found")

elif isinstance(result, str):
    print(result)

else:
    print("Path:", result)
    print("Moves:", len(result) - 1)

    # calculate path cost after BFS finds the path
    path_cost = 0

    for cell in result[1:]:
        path_cost += special_costs.get(cell, 1)

    print("Path cost:", path_cost)
    