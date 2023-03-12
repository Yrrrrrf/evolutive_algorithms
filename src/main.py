"""
Main module for eight_puzzle
Author: Yrrrrrf
"""


#? Imports ------------------------------------------------------------------------------------

# Own imports
from config.globals import Config  # import config
from components.informed_search import *  # import informed search algorithms
from components.uninformed_search import *  #  import uninformed search algorithms
from components.app import App  # import app class
from components.n_puzzle import Puzzle  # import puzzle class


# Import tests
from test.test import Test  #  import test class

#? Logic --------------------------------------------------------------------------------------


def main() -> None:
    """
    Application entry point. 

    It is also responsible for setting up the logging system and configuring it.
    """


    app: App = App()  # create app instance
    # Once created, the app will run until the user closes the window
    # The fisrt thing is to check if the initial state is solvable (also generates the goal state)
    # app.run()  # run app 
    solvable: Puzzle = Puzzle(
        initial_state=[1, 2, 3, 4, 5, 6, 7, 8, 0],
    )  # create puzzle instance

    unsolvable: Puzzle = Puzzle(
        initial_state=[1, 2, 3, 4, 5, 6, 8, 7, 5, 0],
    )  # create puzzle instance


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

