"""
Main module for eight_puzzle
Author: Yrrrrrf
"""


from config.config import Config  # import config
from components.informed_search import *  # import informed search algorithms
from components.uninformed_search import *  #  import uninformed search algorithms
from test.test import Test  #  import test class


def main() -> None:
    """
    Application entry point. 

    It is also responsible for setting up the logging system and configuring it.
    """


    n = int(input("Enter n\n"))
    print("Enter your" ,n,"*",n, "puzzle")
    root = []
    for i in range(0,n*n):
        p = int(input())
        root.append(p)

    print("The given state is:", root)


    #count the number of inversions       
    def inv_num(puzzle):
        inv = 0
        for i in range(len(puzzle)-1):
            for j in range(i+1 , len(puzzle)):
                if (( puzzle[i] > puzzle[j]) and puzzle[i] and puzzle[j]):
                    inv += 1
        return inv

    def solvable(puzzle): #check if initial state puzzle is solvable: number of inversions should be even.
        inv_counter = inv_num(puzzle)
        if (inv_counter %2 ==0):
            return True
        return False


    #1,8,2,0,4,3,7,6,5 is solvable
    #2,1,3,4,5,6,7,8,0 is not solvable


    # else:
    #     print("Not solvable")

    # BFS_solution = BFS(root, n)
    # DFS_solution = DFS(root, n)
    # Greedy_solution = Greedy(root, n)
    # AStar_solution = AStar_search(root, n)


if __name__ == "__main__":
    """
    This is the entry point of the application.
    Clean the terminal and print app data before running the main function.
    """
    print("\033[2J\033[1;1H", end="")  # clear terminal
    print(f"\033[92m{Config.name.value}\033[0m", end=" ")  # print n puzzle solver in green
    print(f"\033[97m{Config.version.value}\033[0m", end="\n\n")  # print version in white

    # Test().run_all()  # run all the tests from the src/test/test.py file
    main()  # run main function

