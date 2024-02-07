'''
title: Paddle subclass / from box parent class
author: Sean Jin
date-created: 05-02-2024
'''
import pygame

from box import Box

class Paddle(Box):
    # Constructor
    def __init__(self, WIDTH=200, HEIGHT=8):
        Box.__init__(self, WIDTH, HEIGHT)
        self._SURFACE = pygame.Surface(self._DIM, pygame.SRCALPHA, 32)
        self._SURFACE.fill(self._COLOR)



if __name__ == "__main__":
    from Window import Window
    pygame.init()
    WINDOW = Window("Test")
    TEST = Paddle(200,8)
    TEST.setPOS(WINDOW.getWidth()//2 - TEST.getWidth()//2, WINDOW.getHeight()//2 - TEST.getHeight()//2+100)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        # INPUTS
        PRESSED_KEYS = pygame.key.get_pressed()
        # PROCESSING
        TEST.ADmove(PRESSED_KEYS)
        WINDOW.clearScreen()
        WINDOW.getSurface().blit(TEST.getSurface(), TEST.getPOS())
        WINDOW.updateFrame()
