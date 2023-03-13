"""
Main module for evolutive algorithms
This module contains the script that launch the GUI that shows the n-puzzle game. (TODO)

Author: Yrrrrrf
Date: Monday 13th, March 2023
"""


#? Imports ------------------------------------------------------------------------------------

# Own imports
from config.globals import Config  # import config
from components import informed_search  # import informed search algorithms
from components import uninformed_search  #  import uninformed search algorithms
from components.app import App  # import app class
from components.n_puzzle import Puzzle  # import puzzle class

# Import tests
from test.unit_test import Test  # import test class


#? Logic --------------------------------------------------------------------------------------


def main() -> None:
    """
    Application entry point. 

    It is also responsible for setting up the logging system and configuring it.
    """
    # Once created, the app will run until the user closes the window
    # app: App = App()  # create app instance
    # app.run()  # run app

    # The fisrt thing is to check if the initial state is solvable (also generates the goal state)
    solvable: Puzzle = Puzzle(initial_state=[1, 2, 3, 4, 5, 6, 7, 8, 0],)  # create puzzle instance
    unsolvable: Puzzle = Puzzle(initial_state=[1, 2, 3, 4, 5, 6, 8, 7, 0],)  # create puzzle instance

    # excetuce the informed_algorithms.py file main function


if __name__ == "__main__":
    """
    This is the entry point of the application.
    Clean the terminal and print app data before running the main function.
    """
    print("\033[2J\033[1;1H", end="")  # clear terminal
    print(f"\033[92m{Config.NAME.value}\033[0m", end=" ")  # print n puzzle solver in green
    print(f"\033[97m{Config.VERSION.value}\033[0m", end="\n\n")  # print version in white

    # Test().run_all()  # run all the tests from the src/test/test.py file
    main()  # run main function


# Laberinths
# 8 Queens
# 8 Puzzle (3x3)
# (n^2)-1 Puzzle (nxn)

