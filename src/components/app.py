"""
App module

This module contains the script that launch the GUI that shows the n-puzzle game.
"""

#? Imports ------------------------------------------------------------------------------------

# Python imports
import pygame
import random
import time
from dataclasses import dataclass  # dataclass decorator

# Own imports
from config.globals import Config, Theme
from components.informed_search import *  # import informed search algorithms
from components.uninformed_search import *  #  import uninformed search algorithms


#? Logic --------------------------------------------------------------------------------------


#  create app class
@dataclass
class App:
    """
    App class
    This class contains the logic for the GUI
    """
    # App data (App State)
    screen: pygame.Surface
    running: bool = True
    play: bool = True


    def __init__(self) -> None:
        """
        Initialize the app
        """
        print("Welcome to the 8 puzzle solver.")
    #     self.shuffle_time = 0
    #     self.start_shuffle = False
    #     self.previous_choice = ""
    #     self.start_game = False
    #     self.start_timer = False
    #     self.elapsed_time = 0
    #     self.high_score = float(self.get_high_scores()[0])




        # Ask for the puzzle size

        # Ask for the initial state

        # Goal State is always 1,2,3,4,5,6,7,8,0
        # todo: implement custom goal state


        # run the tests for the uninformed search algorithms
        # print("Uninformed Search Algorithms")
        # BFS_test()
        # DFS_test()
        # print("Informed Search Algorithms")
        # Greedy_test()
        # AStar_test()
        # ...



        # n = int(input("Enter n\n"))
        # print("Enter your" ,n,"*",n, "puzzle")
        # root = []
        # for i in range(0,n*n):
        #     p = int(input())
        #     root.append(p)

        # print("The given state is:", root)


        # #count the number of inversions       
        # def inv_num(puzzle):
        #     inv = 0
        #     for i in range(len(puzzle)-1):
        #         for j in range(i+1 , len(puzzle)):
        #             if (( puzzle[i] > puzzle[j]) and puzzle[i] and puzzle[j]):
        #                 inv += 1
        #     return inv

        # def solvable(puzzle): #check if initial state puzzle is solvable: number of inversions should be even.
        #     inv_counter = inv_num(puzzle)
        #     if (inv_counter %2 ==0):
        #         return True
        #     return False


        #1,8,2,0,4,3,7,6,5 is solvable
        #2,1,3,4,5,6,7,8,0 is not solvable


        # else:
        #     print("Not solvable")

        # BFS_solution = BFS(root, n)
        # DFS_solution = DFS(root, n)
        # Greedy_solution = Greedy(root, n)
        # AStar_solution = AStar_search(root, n)


    def run(self) -> None:
        """
        Pop up the window and run the app while the user doesn't close the window
        """
        pygame.init()  # initialize pygame
        self.screen = pygame.display.set_mode((Config.WIDTH.value, Config.HEIGHT.value))  # set window size
        pygame.display.set_caption(f"{Config.NAME.value} {Config.VERSION.value}")  # set window title
        pygame.display.set_icon(pygame.image.load("resources/img/puzzle.png"))

        self.clock = pygame.time.Clock()  # Initialize the clock

        while self.running:
            self.clock.tick(60)  # set the fps to 60

            for event in pygame.event.get():  # get all events
                if event.type == pygame.QUIT:  # if the user clicks the close button
                    pygame.quit()  # quit pygame
                    exit()  # exit the program
            if self.play:  # if the game is running
                self.screen.fill(Theme.BACKGROUND.value)  # fill the screen with the background color
                # render_points(cube_coordinates, window, True, active_edges[selected_edge])  # render the points
                # HERE GOES THE GAME LOGIC...
                # render the screen...
            pygame.display.update()  # update the display

