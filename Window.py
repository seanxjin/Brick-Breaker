'''
title: pygame template file
author: Sean Jin
date-created: 04-02-2024
'''

import pygame

class Window:
    """
    This creates a window that serves as the foundation for the brick breaker game
    """
    def __init__(self, TITLE, WIDTH=1100, HEIGHT=700, FPS=60):
        self.__TITLE = TITLE
        self.__WIDTH = WIDTH
        self.__HEIGHT = HEIGHT
        self.__SCREEN_DIMENSION = (self.__WIDTH, self.__HEIGHT)
        self.__CLOCK = pygame.time.Clock()
        self.__SURFACE = pygame.display.set_mode(self.__SCREEN_DIMENSION)
        self.__SURFACE.fill((0,0,0))
        self.__FPS = FPS
        pygame.display.set_caption(self.__TITLE)

    # MODIFIER METHODS
    def updateFrame(self):
        """
        Updates the window and controls the frame rate of the window
        :return: none
        """
        self.__CLOCK.tick(self.__FPS)
        pygame.display.flip()

    def clearScreen(self):
        """
        Clears the screen of the window, or in other words, just re-fills the surface back to all black color
        :return: none
        """
        self.__SURFACE.fill((0,0,0))
    # ACCESSOR METHODS
    def getSurface(self):
        """
        returns the surface of the window, initializes the screen.
        :return: obj
        """
        return self.__SURFACE

    def getWidth(self):
        """
        returns the width of the window
        :return: int
        """
        return self.__WIDTH

    def getHeight(self):
        """
        returns Height of the window
        :return: int
        """
        return self.__HEIGHT

