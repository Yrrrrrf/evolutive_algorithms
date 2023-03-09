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

    # Misc
    # pygame.font.init()
    # font = pygame.font.SysFont("Consolas", 30)
    # font2 = pygame.font.SysFont("Consolas", 20)
    # font3 = pygame.font.SysFont("Consolas", 15)
    # font4 = pygame.font.SysFont("Consolas", 10)
    # font5 = pygame.font.SysFont("Consolas", 50)
    # font6 = pygame.font.SysFont("Consolas", 40)
    # font7 = pygame.font.SysFont("Consolas", 25)


    def __init__(self) -> None:
        """
        Initialize the app
        """

        pygame.init()  # initialize pygame
        self.screen = pygame.display.set_mode((Config.WIDTH.value, Config.HEIGHT.value))  # set window size
        pygame.display.set_caption(f"{Config.NAME.value} {Config.VERSION.value}")  # set window title
        pygame.display.set_icon(pygame.image.load("resources/img/puzzle.png"))

        self.clock = pygame.time.Clock()  # Initialize the clock


        while self.running:
            self.clock.tick(60)

            for event in pygame.event.get():  # get all events
                if event.type == pygame.QUIT:  # if the user clicks the close button
                    pygame.quit()  # quit pygame
                    exit()  # exit the program
            if self.play:  # if the game is running
                self.screen.fill(Theme.BACKGROUND.value)  # fill the screen with the background color
                # render_points(cube_coordinates, window, True, active_edges[selected_edge])  # render the points
            pygame.display.update()




    # def __post_init__(self):
    #     """
    #     Post initialization
    #     """
    #     self.run()  # run the app


    # def __init__(self):

    #     self.shuffle_time = 0
    #     self.start_shuffle = False
    #     self.previous_choice = ""
    #     self.start_game = False
    #     self.start_timer = False
    #     self.elapsed_time = 0
    #     self.high_score = float(self.get_high_scores()[0])


