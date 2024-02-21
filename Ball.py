'''
title: Ball subclass from box parent class
author: Sean Jin
date-created: 05-02-2024
'''

from box import Box
import pygame

class Ball(Box):
    def __init__(self, WIDTH=2, HEIGHT=2):
        Box.__init__(self, WIDTH, HEIGHT)
        self._SURFACE = pygame.Surface(self._DIM, pygame.SRCALPHA, 32)
        self._SURFACE.fill(self._COLOR)

    # MODIFIER METHODS
    def setWidth(self, WIDTH):
        Box.setWidth(self, WIDTH)
        self._SURFACE = pygame.Surface(self._DIM, pygame.SRCALPHA, 32)

    def setHeight(self, HEIGHT):
        Box.setHeight(self,HEIGHT)
        self._SURFACE = pygame.Surface(self._DIM, pygame.SRCALPHA, 32)
    def setDim(self, WIDTH, HEIGHT):
        self.setWidth(WIDTH)
        self.setHeight(HEIGHT)
        self._SURFACE.fill(self._COLOR)
    def isCollision(self, SURFACE, POS):
        """
        Boolean function that checks if a current sprites position is overlapping with another sprite
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



if __name__ == "__main__":
    from Window import Window
    pygame.init()
    WINDOW = Window("Ball Test")
    BALL = Ball()
    BALL.setDim(5,5)
    BALL.setPOS(WINDOW.getWidth()//2 - BALL.getWidth()//2, WINDOW.getHeight()//2 - BALL.getHeight()//2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


        WINDOW.clearScreen()
        WINDOW.getSurface().blit(BALL.getSurface(), BALL.getPOS())
        BALL.bounceXandY(WINDOW.getWidth(), WINDOW.getHeight())
        WINDOW.updateFrame()

