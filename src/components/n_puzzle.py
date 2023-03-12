# n puzzle logic

#check if initial state puzzle is solvable: number of inversions should be even.    

#? Imports ------------------------------------------------------------------------------------

from dataclasses import dataclass
import colorama


#? Logic --------------------------------------------------------------------------------------

@dataclass
class Puzzle:
    """
    A class to represent a puzzle state.
    """
    initial_state: list  # the initial state of the puzzle
    goal_state: list  # the goal state of the puzzle
    n: int  # the size of the puzzle

    # the following methods are used to define the puzzle
    parent: object  # the parent of the current state
    path_cost: int  # the path cost of the current state


    def __init__(
            self,  # the constructor
            initial_state: list,  # Solvable
            # goal_state: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 0]],
            n: int = 3  # the size of the puzzle
            ) -> None:
        """
        The constructor of the class
        """
        self.initial_state = initial_state  # set the initial state
        if len(self.initial_state) != n ** 2: raise ValueError(f'The initial state is not a square matrix')
        else: self.n = n  # set the size of the puzzle

        self.describe()  # describe the puzzle


    # override the to string method
    def describe(self) -> None:
        """
        Describe the puzzle
        
        Prints the initial state of the puzzle
        Also prints if the puzzle is solvable
        """
        # print if the puzzle is solvable
        print(f'\nGrid is {colorama.Fore.GREEN if self.is_solvable(self.initial_state) else colorama.Fore.RED}{"solvable" if self.is_solvable(self.initial_state) else "not solvable"}{colorama.Style.RESET_ALL}')
        # print the initial state in a matrix form
        [print(self.initial_state[i * self.n:(i + 1) * self.n]) for i in range(self.n)]


    def is_solvable(self, puzzle: list) -> bool:
        """Check if the puzzle is solvable"""
        inv_counter = self.inv_num(puzzle)
        if (inv_counter % 2 == 0):
            return True
        return False
    

    def inv_num(self, puzzle: list) -> int:
        """Count the number of inversions"""
        inv = 0
        for i in range(len(puzzle) - 1):
            for j in range(i + 1, len(puzzle)):
                if ((puzzle[i] > puzzle[j]) and puzzle[i] and puzzle[j]):
                    inv += 1
        return inv
    
