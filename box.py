'''
title: Box parent class
author: Sean Jin
date-created: 04-02-2024
'''

import pygame
import random
class Box:
    """
    This creates a parent class of a white box that is going to be inherited by other subclasses
    """
    def __init__(self, WIDTH=100, HEIGHT=36, X=0,Y=0, SPEED=5, COLOR=(255,255,255)):
        self.__WIDTH = WIDTH
        self.__HEIGHT = HEIGHT
        self._DIM = (self.__WIDTH, self.__HEIGHT)
        self.__X = X
        self.__Y = Y
        self.__POS = (self.__X, self.__Y)
        self.__SPEED = SPEED
        self._COLOR = COLOR
        self._SURFACE = pygame.Surface
        self.__DIR_X = random.choice([1, -1])
        self.__DIR_Y = 1

    # MODIFIER METHODS
    def WASDmove(self, KEY_PRESSES):
        """
        Move the box based on WASD
        :param HEY_PRESSES: list[int]
        :return: none
        """
        if KEY_PRESSES[pygame.K_d] == 1:
            self.__X = self.__X - self.__SPEED
        if KEY_PRESSES[pygame.K_a] == 1:
            self.__X = self.__X + self.__SPEED
        if KEY_PRESSES[pygame.K_w] == 1:
            self.__Y = self.__Y + self.__SPEED
        if KEY_PRESSES[pygame.K_s] == 1:
            self.__Y = self.__Y - self.__SPEED
        self.__POS = (self.__X, self.__Y)
    def setX(self,X):
        """
        Sets the X position of the object
        :return: none
        """
        self.__X = X
        self.__POS = (self.__X, self.__Y)

    def setY(self, Y):
        """
        Sets theY position of the object
        :return: none
        """
        self.__Y = Y
        self.__POS = (self.__X, self.__Y)

    def setPOS(self, X, Y):
        """
        Sets the position of the object
        :param X: int
        :param Y: int
        :return: none
        """
        self.setX(X)
        self.setY(Y)

    def setColor(self, TUPLE):
        """
        Sets the color of the object
        :param TUPLE: tuple[int]
        :return: none
        """
        self._COLOR = TUPLE

    def setWidth(self, WIDTH):
        """
        Sets the width of the object
        :param WIDTH: int
        :return: none
        """
        self.__WIDTH = WIDTH
        self._DIM = (self.__WIDTH, self.__HEIGHT)

    def setHeight(self, HEIGHT):
        """
        Sets the height of the object
        :param HEIGHT: int
        :return: none
        """
        self.__HEIGHT = HEIGHT
        self._DIM = (self.__WIDTH, self.__HEIGHT)

    def setDim(self, WIDTH, HEIGHT):
        """
        Sets the dimension/size of the object
        :param WIDTH: int
        :param HEIGHT: int
        :return: none
        """
        self.setWidth(WIDTH)
        self.setHeight(HEIGHT)
    def setSpeed(self, SPEED):
        """
        Sets the speed of the object
        :param SPEED: int
        :return: none
        """
        self.__SPEED = SPEED
    def bounceXandY(self, MAX_X, MAX_Y, MIN_Y=0, MIN_X=0):
        """
        Bounces the obj when hitting its x and y boundaries
        :param MAX_X: int
        :param MAX_Y: int
        :param MIN_Y: int
        :param MIN_X: int
        :return: none
        """
        self.__X = self.__X + self.__SPEED * self.__DIR_X
        self.__Y = self.__Y + self.__SPEED * self.__DIR_Y
        if self.__X > MAX_X - self.getWidth():
            self.__DIR_X = -1
        if self.__X < MIN_X:
            self.__DIR_X = 1
        if self.__Y > MAX_Y - self.getHeight():
            self.__DIR_Y = -1
        if self.__Y < MIN_Y:
            self.__DIR_Y = 1
        self.__POS = (self.__X, self.__Y)
    def isCollision(self, SURFACE, POS):
        """
        Boolean function that checks if an current sprites position is overlapping with another sprite
        :param SURFACE: object
        :param POS: tuple -> int
        :return: bool
        """
        WIDTH = SURFACE.get_width()
        HEIGHT = SURFACE.get_height()
        X = POS[0]
        Y = POS[1]
        if X >= self.__X - WIDTH and X <= self.__X + self._SURFACE.get_width():
            if Y >= self.__Y - HEIGHT and Y <= self.__Y + self._SURFACE.get_height():
                return True
        return False
    def wrapEdges(self, MAX_X, MAX_Y, MIN_X=0, MIN_Y=0):
        """
        When the object goes off the screen, it appears on the side of the screen
        :param MAX_X: int
        :param MAX_Y: int
        :param MIN_X: int
        :param MIN_Y: int
        :return: none
        """
        if self.__X > MAX_X - self.__WIDTH:
            self.__X = MIN_X
        if self.__X < MIN_X:
            self.__X = MAX_X
        if self.__Y > MAX_Y + self.__HEIGHT:
            self.__Y = MIN_Y
        if self.__Y < MIN_Y:
            self.__Y = MAX_Y
    # ACCESSOR METHODS
    def getX(self):
        """
        returns the X position of the object
        :return: int
        """
        return self.__X
    def getY(self):
        """
        returns the Y positions of the object
        :return: int
        """
        return self.__Y

    def getWidth(self):
        """
        returns the width of the object
        :return: int
        """
        return self._SURFACE.get_width()
    def getHeight(self):
        """
        returns the height of the object
        :return: int
        """
        return self._SURFACE.get_height()

    def getDim(self):
        """
        returns the dimension / size of the object
        :return: tuple
        """
        return self._DIM

    def getPOS(self):
        """
        returns the position of the object
        :return: tuple
        """
        return self.__POS
    def getSurface(self):
        """
        Gets the surface of the object
        :return: obj
        """
        return self._SURFACE
    def getSpeed(self):
        """
        Gets the speed of the object
        :return: int
        """
        return self.__SPEED