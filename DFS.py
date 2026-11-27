
def dfs(start, goal, rows, columns, obstacles):

    # Check start and goal boundaries
    if not (0 <= start[0] < columns and 0 <= start[1] < rows):
        return "Invalid start coordinates"

    if not (0 <= goal[0] < columns and 0 <= goal[1] < rows):
        return "Invalid goal coordinates"

    # Check obstacles
    if start in obstacles:
        return "Start position is blocked by an obstacle"

    if goal in obstacles:
        return "Goal position is blocked by an obstacle"

    queue = [[start]]

    while queue:
        path = queue.pop()
        node = path[-1]

        if node == goal:
            return path

        else:
            x, y = node

            adjacent_nodes = [
                (x+1, y),
                (x-1, y),
                (x, y+1),
                (x, y-1)
            ]

            for adjacent_node in adjacent_nodes:
                nx, ny = adjacent_node

                if (0 <= nx < columns and 0 <= ny < rows
                        and adjacent_node not in obstacles
                        and adjacent_node not in path):

                    new_path = list(path)
                    new_path.append(adjacent_node)
                    queue.append(new_path)

    return None


# Get maze dimensions
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))


# Get start and goal
start_x, start_y = input("Enter start coordinates (x,y): ").split(",")
goal_x, goal_y = input("Enter goal coordinates (x,y): ").split(",")

start = (int(start_x), int(start_y))
goal = (int(goal_x), int(goal_y))


# Get obstacles
obstacles = set()

number_of_obstacles = int(input("Enter number of obstacles: "))

for i in range(number_of_obstacles):
    obstacle_x, obstacle_y = input("Enter obstacle coordinates (x,y): ").split(",")
    obstacles.add((int(obstacle_x), int(obstacle_y)))


# Get special costs
special_costs = {}

number_of_special_nodes = int(input("Enter number of special-cost nodes: "))

for i in range(number_of_special_nodes):
    special_x, special_y = input("Enter special node coordinates (x,y): ").split(",")
    special_cost = int(input("Enter the cost of this node: "))

    special_costs[(int(special_x), int(special_y))] = special_cost


# Run DFS
result = dfs(start, goal, rows, columns, obstacles)


# Display result and calculate cost
if result is None:
    print("No path found")

elif isinstance(result, str):
    print(result)

else:
    print("Path:", result)
    print("Moves:", len(result) - 1)

    path_cost = 0

    for cell in result[1:]:
        path_cost += special_costs.get(cell, 1)

    print("Path cost:", path_cost)
