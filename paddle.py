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

    def WASDmove(self, KEYS_PRESSED):
        """
        Allows the paddle to be moved through WASD
        :param KEYS_PRESSED: list[int]
        :return: none
        """
        if KEYS_PRESSED[pygame.K_d] == 1:
            self.setX(self.getX()+self.getSpeed())
        if KEYS_PRESSED[pygame.K_a] == 1:
            self.setX(self.getX()-self.getSpeed())
    def checkBoundaries(self, MAX_X, MIN_X=0):
        """
        Checks the bounderies of the paddle and prevents it from going offscreen
        :param MAX_X: int
        :param MIN_X: int
        :return: none
        """
        if self.getX() > MAX_X - self.getWidth():
            self.setX(MAX_X - self.getWidth())
        if self.getX() < MIN_X:
            self.setX(MIN_X)
if __name__ == "__main__":
    from Window import Window
    pygame.init()
    WINDOW = Window("PADDLE")
    PADDLE = Paddle(200,8)
    PADDLE.setPOS(WINDOW.getWidth()//2 - PADDLE.getWidth()//2, WINDOW.getHeight()//2 - PADDLE.getHeight()//2+100)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        # INPUTS
        PRESSED_KEYS = pygame.key.get_pressed()
        # PROCESSING
        PADDLE.WASDmove(PRESSED_KEYS)
        PADDLE.checkBoundaries(WINDOW.getWidth())
        WINDOW.clearScreen()
        WINDOW.getSurface().blit(PADDLE.getSurface(), PADDLE.getPOS())
        WINDOW.updateFrame()
