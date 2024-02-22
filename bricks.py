'''
title: Bricks subclass inherited from the box parent class
author: Sean Jin
date-created: 05-02-2024
'''

from box import Box
import pygame
class Bricks(Box):
    def __init__(self):
        Box.__init__(self)
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
        # Polymorphism from the parent class box
        # Only checks if the 2 sprites collide with one another
        WIDTH = SURFACE.get_width()
        HEIGHT = SURFACE.get_height()
        X = POS[0]
        Y = POS[1]
        if X >= self.getX() - WIDTH and X <= self.getX() + self.getWidth() and Y >= self.getY() - HEIGHT and Y <= self.getY() + self.getHeight():
            # Checks which side the sprites collide on
            OVERLAP_LEFT = abs((self.getX() - WIDTH) - X) # Closest to the left side
            OVERLAP_RIGHT = abs((self.getX() + self.getWidth()) - X) # Closest to the right side
            OVERLAP_TOP = abs((self.getY() - HEIGHT) - Y) # Closest to the top side
            OVERLAP_BOTTOM = abs((self.getY() + self.getHeight()) - Y) # Closest to the bottom side
            # Checks the smallest value/distance between the sides to determine which side it hits
            MIN_OVERLAP = min(OVERLAP_LEFT, OVERLAP_RIGHT, OVERLAP_TOP, OVERLAP_BOTTOM)
            if MIN_OVERLAP == OVERLAP_LEFT:
                return 1
            elif MIN_OVERLAP == OVERLAP_RIGHT:
                return 2
            elif MIN_OVERLAP == OVERLAP_TOP:
                return 3
            elif MIN_OVERLAP == OVERLAP_BOTTOM:
                return 4
            else:
                return 5
        else:
            pass
if __name__ == "__main__":
    from Window import Window
    pygame.init()
    WINDOW = Window("Brick Test")
    BRICKLIST = []
    for i in range(6):
        ROW = []
        offset_x = 120 if i % 2 == 0 else 180  # Adjust offset_x based on i
        for j in range(6):
            ADDBRICK = Bricks()
            ADDBRICK.setDim(120, 40)
            ADDBRICK.setPOS(offset_x + j * 125, 40 + i * 45)
            ROW.append(ADDBRICK)
        BRICKLIST.append(ROW)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        WINDOW.clearScreen()
        for i in range(len(BRICKLIST)):
            for j in range(len(BRICKLIST[i])):
                WINDOW.getSurface().blit(BRICKLIST[i][j].getSurface(), BRICKLIST[i][j].getPOS())
        WINDOW.updateFrame()

