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

