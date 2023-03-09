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

