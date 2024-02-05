'''
title: Box parent class
author: Sean Jin
date-created: 04-02-2024
'''

import pygame
class Box:
    """
    This creates a parent class of a white box that is going to be inherited by other subclasses
    """
    def __init__(self, WIDTH=1, HEIGHT=1, X=0,Y=0, SPEED=5, COLOR=(255,255,255)):
        self.__WIDTH = WIDTH
        self.__HEIGHT = HEIGHT
        self._DIM = (self.__WIDTH, self.__HEIGHT)
        self.__X = X
        self.__Y = Y
        self.__POS = (self.__X, self.__Y)
        self.__SPEED = SPEED
        self._COLOR = COLOR
        self._SURFACE = pygame.Surface
        self.__DIR_X = 1
        self.__DIR_Y = 1

    # MODIFIER METHODS
    def WASDmove(self, KEYS_PRESSED):
        """
        Allows the box to be moved through WASD
        :param KEYS_PRESSED: list[int]
        :return: none
        """
        if KEYS_PRESSED[pygame.K_d] == 1:
            self.__X = self.__X + self.__SPEED
        if KEYS_PRESSED[pygame.K_a] == 1:
            self.__X = self.__X - self.__SPEED
        if KEYS_PRESSED[pygame.K_w] == 1:
            self.__Y = self.__Y - self.__SPEED
        if KEYS_PRESSED[pygame.K_s] == 1:
            self.__Y = self.__Y + self.__SPEED
        self.__POS = (self.__X, self.__Y)

    def setX(self,X):
        """
        Sets the X position of the object
        :return: none
        """



