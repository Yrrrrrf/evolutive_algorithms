import unittest  # import unittest


class Test(unittest.TestCase):
    """
    Test class for the eight_puzzle application
    """
    def test(self):  #  implement the test function
        """
        Test function
        """
        self.assertTrue(True)  #  assert that the test is true


    def run_all(self):
        """
        Run all the tests
        """
        self.test_informed_search()  #  run the test function
        self.test_uninformed_search()  #  run the test function


#? Uinformed Search Algorithms ------------------------------------------------------------------------------------------------


    def test_informed_search(self):
        """
        Test function for informed search algorithms
        """


        def h(state, goal_state):
            """
            Heuristic function
            """
            pass


        def g(state, goal_state):
            """
            Cost function
            """
            pass

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


        def greedy_best_first_search(state, goal_state, h):
            """
            Greedy Best First Search Algorithm

            :param state: the initial state
            :param goal_state: the goal state
            :param h: the heuristic function
            :return: the solution, the number of explored nodes
            """
            pass


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


        def recursive_best_first_search(state, goal_state, h):
            """
            Recursive Best First Search Algorithm

            :param state: the initial state
            :param goal_state: the goal state
            :param h: the heuristic function
            :return: the solution, the number of explored nodes
            """
            pass



#? Uinformed Search Algorithms ------------------------------------------------------------------------------------------------


    def test_uninformed_search(self):
        """
        Test function for uninformed search algorithms
        """
        pass


    def test_breadth_first_search(self):
        """
        Test function for breadth first search algorithm
        """
        pass


    def test_depth_first_search(self):
        """
        Test function for depth first search algorithm
        """
        pass


    def test_iterative_deepening_search(self):
        """
        Test function for iterative deepening search algorithm
        """
        pass



    

if __name__ == '__main__':
    unittest.main()   # Run the test
