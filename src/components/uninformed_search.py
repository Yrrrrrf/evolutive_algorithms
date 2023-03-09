"""
Uninformed Search Algorithms

Uninformed search algorithms are a subclass of the general search algorithms.
They do not use any heuristics to guide the search towards the goal state.
They are less efficient than informed search algorithms.

- Breadth First Search
- Depth First Search
- Iterative Deepening Depth First Search
- Uniform Cost Search
- Depth Limited Search
- Iterative Deepening Depth Limited Search
- Bidirectional Search
- Bidirectional Depth Limited Search
- Iterative Deepening Bidirectional Search
- Iterative Deepening Bidirectional Depth Limited Search
- Iterative Deepening A* Search
"""


from test.performance import performance  # import performance decorator


@performance  # print the time it took to execute the function
def breadth_first_search(state, goal_state):
    """
    Breadth First Search Algorithm

    :param state: the initial state
    :param goal_state: the goal state
    :return: the solution, the number of explored nodes
    """
    pass


@performance  # print the time it took to execute the function
def depth_first_search(state, goal_state):
    """
    Depth First Search Algorithm

    :param state: the initial state
    :param goal_state: the goal state
    :return: the solution, the number of explored nodes
    """
    pass


@performance  # print the time it took to execute the function
def iterative_deepening_depth_first_search(state, goal_state):
    """
    Iterative Deepening Depth First Search Algorithm

    :param state: the initial state
    :param goal_state: the goal state
    :return: the solution, the number of explored nodes
    """
    pass


@performance  # print the time it took to execute the function
def uniform_cost_search(state, goal_state, g):
    """
    Uniform Cost Search Algorithm

    :param state: the initial state
    :param goal_state: the goal state
    :param g: the cost function
    :return: the solution, the number of explored nodes
    """
    pass


@performance  # print the time it took to execute the function
def depth_limited_search(state, goal_state, limit):
    """
    Depth Limited Search Algorithm

    :param state: the initial state
    :param goal_state: the goal state
    :param limit: the depth limit
    :return: the solution, the number of explored nodes
    """
    pass


@performance  # print the time it took to execute the function
def iterative_deepening_depth_limited_search(state, goal_state, limit):
    """
    Iterative Deepening Depth Limited Search Algorithm

    :param state: the initial state
    :param goal_state: the goal state
    :param limit: the depth limit
    :return: the solution, the number of explored nodes
    """
    pass


