
def ucs(start, goal, rows, columns, obstacles, special_costs):

    # check if start and goal are within grid boundaries and not blocked by obstacles
    if not (0 <= start[0] <= columns - 1 and 0 <= start[1] <= rows - 1):
        return "Invalid start coordinates"

    if not (0 <= goal[0] <= columns - 1 and 0 <= goal[1] <= rows - 1):
        return "Invalid goal coordinates"

    if start in obstacles:
        return "Start position is blocked by an obstacle"

    if goal in obstacles:
        return "Goal position is blocked by an obstacle"

    queue = [(0, start, [start])]  # cost, current node, path
    best_cost = {start: 0}
    visited = set()

    while queue:

        queue.sort()
        cost, node, path = queue.pop(0)

        if cost != best_cost.get(node):
            continue # skip if a cheaper one has already been found

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return path, cost

        x, y = node

        neighbors = [
            (x+1, y),
            (x-1, y),
            (x, y+1),
            (x, y-1)
        ]

        for neighbor in neighbors:

            nx, ny = neighbor

            # check for grid boundaries and obstacles
            if (0 <= nx <= columns - 1 and 0 <= ny <= rows - 1 and neighbor not in obstacles):

                if neighbor not in visited:

                    movement_cost = special_costs.get(neighbor, 1)   # if no movement cost is specified, cost is 1
                    new_cost = cost + movement_cost

                    if new_cost < best_cost.get(neighbor, float('inf')): # if the neighbor has no recorded cost assume infinity (use new_cost)

                        best_cost[neighbor] = new_cost

                        queue.append((
                            new_cost,
                            neighbor,
                            path + [neighbor]
                        ))

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

special_costs = {}

number_of_special_nodes = int(input("Enter number of special-cost nodes: "))

for i in range(number_of_special_nodes):
    special_x, special_y = input("Enter special node coordinates (x,y): ").split(",")
    special_cost = int(input("Enter the cost of this node: "))

    special_costs[(int(special_x), int(special_y))] = special_cost

result = ucs(start, goal, rows, columns, obstacles, special_costs)

if result is None:
    print("No path found")

elif isinstance(result, str): # error messages
    print(result)

else:
    print("Path:", result[0])
    print("Total Cost:", result[1])