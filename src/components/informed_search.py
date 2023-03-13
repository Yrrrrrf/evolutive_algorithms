"""
Informed Search Algorithms

Informed search algorithms are a subclass of the general search algorithms.
They use heuristics to guide the search towards the goal state.
They are more efficient than uninformed search algorithms.

- Greedy Best First Search
- A* Search
- Iterative Deepening A* Search
- Recursive Best First Search
- IDA* Search
- Hill Climbing Search
- Simulated Annealing Search
- Genetic Algorithm Search
- Ant Colony Optimization Search
- Particle Swarm Optimization Search
- Tabu Search
- Variable Neighborhood Search
- Variable Neighborhood Descent Search

"""


from test.performance import performance  # import performance decorator


@performance  # print the time it took to execute the function
def a_star(state, goal_state, h, g):
    """
    A* Search Algorithm

    :param state: the initial state
    :param goal_state: the goal state
    :param h: the heuristic function
    :param g: the cost function
    :return: the solution, the number of explored nodes
    """
    pass



@performance  # print the time it took to execute the function
def greedy_best_first_search(state, goal_state, h):
    """
    Greedy Best First Search Algorithm

    :param state: the initial state
    :param goal_state: the goal state
    :param h: the heuristic function
    :return: the solution, the number of explored nodes
    """
    pass



@performance  # print the time it took to execute the function
def iterative_deepening_a_star(state, goal_state, h, g):
    """
    Iterative Deepening A* Search Algorithm

    :param state: the initial state
    :param goal_state: the goal state
    :param h: the heuristic function
    :param g: the cost function
    :return: the solution, the number of explored nodes
    """
    pass


@performance  # print the time it took to execute the function
def recursive_best_first_search(state, goal_state, h):
    """
    Recursive Best First Search Algorithm

    :param state: the initial state
    :param goal_state: the goal state
    :param h: the heuristic function
    :return: the solution, the number of explored nodes
    """
    pass


@performance  # print the time it took to execute the function
def ida_star(state, goal_state, h, g):
    """
    IDA* Search Algorithm

    :param state: the initial state
    :param goal_state: the goal state
    :param h: the heuristic function
    :param g: the cost function
    :return: the solution, the number of explored nodes
    """
    pass


@performance  # print the time it took to execute the function
def hill_climbing_search(state, goal_state, h):
    """
    Hill Climbing Search Algorithm

    :param state: the initial state
    :param goal_state: the goal state
    :param h: the heuristic function
    :return: the solution, the number of explored nodes
    """
    pass


@performance  # print the time it took to execute the function
def simulated_annealing_search(state, goal_state, h):
    """
    Simulated Annealing Search Algorithm

    :param state: the initial state
    :param goal_state: the goal state
    :param h: the heuristic function
    :return: the solution, the number of explored nodes
    """
    pass



DIRECTIONS = [
    [-1, 0],  # left
    [0, -1],  # down
    [1, 0],  # right
    [0, 1],  # up
]


# function to search the path
def search(
    grid: list[list[int]],
    init: list[int],
    goal: list[int],
    cost: int,
    heuristic: list[list[int]],
) -> tuple[list[list[int]], list[list[int]]]:
    closed = [
        [0 for col in range(len(grid[0]))] for row in range(len(grid))
    ]  # the reference grid
    closed[init[0]][init[1]] = 1
    action = [
        [0 for col in range(len(grid[0]))] for row in range(len(grid))
    ]  # the action grid

    x = init[0]
    y = init[1]
    g = 0
    f = g + heuristic[x][y]  # cost from starting cell to destination cell
    cell = [[f, g, x, y]]

    found = False  # flag that is set when search is complete
    resign = False  # flag set if we can't find expand

    while not found and not resign:
        if len(cell) == 0:
            raise ValueError("Algorithm is unable to find solution")
        else:  # to choose the least costliest action so as to move closer to the goal
            cell.sort()
            cell.reverse()
            next_cell = cell.pop()
            x = next_cell[2]
            y = next_cell[3]
            g = next_cell[1]

            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(DIRECTIONS)):  # to try out different valid actions
                    x2 = x + DIRECTIONS[i][0]
                    y2 = y + DIRECTIONS[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            f2 = g2 + heuristic[x2][y2]
                            cell.append([f2, g2, x2, y2])
                            closed[x2][y2] = 1
                            action[x2][y2] = i
    invpath = []
    x = goal[0]
    y = goal[1]
    invpath.append([x, y])  # we get the reverse path from here
    while x != init[0] or y != init[1]:
        x2 = x - DIRECTIONS[action[x][y]][0]
        y2 = y - DIRECTIONS[action[x][y]][1]
        x = x2
        y = y2
        invpath.append([x, y])

    path = []
    for i in range(len(invpath)):
        path.append(invpath[len(invpath) - 1 - i])
    return path, action


if __name__ == "__main__":
    grid = [
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],  # 0 are free path whereas 1's are obstacles
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0],
    ]

    init = [0, 0]
    # all coordinates are given in format [y,x]
    goal = [len(grid) - 1, len(grid[0]) - 1]
    cost = 1

    # the cost map which pushes the path closer to the goal
    heuristic = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            heuristic[i][j] = abs(i - goal[0]) + abs(j - goal[1])
            if grid[i][j] == 1:
                # added extra penalty in the heuristic map
                heuristic[i][j] = 99

    path, action = search(grid, init, goal, cost, heuristic)

    print("ACTION MAP")
    for i in range(len(action)):
        print(action[i])

    for i in range(len(path)):
        print(path[i])


    # print the path
    x = init[0]
    y = init[1]
    grid[x][y] = 2
    for i in range(len(path)):
        x = path[i][0]
        y = path[i][1]
        grid[x][y] = 3
    grid[goal[0]][goal[1]] = 4

    for i in range(len(grid)):
        print(grid[i])
        
    print("PATH")
    for i in range(len(path)):
        print(path[i])
        
    print("ACTION MAP")
    for i in range(len(action)):
        print(action[i])

