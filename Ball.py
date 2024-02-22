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
    def initiateBallMove(self):
        """
        Initiates the movement of the ball
        :return: none
        """
        self.setX(self.getX() + self.getSpeed() * self.getDirX())
        self.setY(self.getY() + self.getSpeed() * self.getDirY())
    def bounceXandY(self, MAX_X, MIN_Y=0, MIN_X=0):
        """
        Bounces the obj when hitting its x and y boundaries
        :param MAX_X: int
        :param MAX_Y: int
        :param MIN_Y: int
        :param MIN_X: int
        :return: none
        """
        if self.getX() > MAX_X - self.getWidth():
            self.setDirX(-1)
        if self.getX() < MIN_X:
            self.setDirX(1)
        if self.getY() < MIN_Y:
            self.setDirY(1)
        self.setPOS(self.getX(), self.getY())
    def collideBouncePaddle(self, KEYS_PRESSED):
        """
        How the ball behaves when bouncing with the paddle
        :param SIDE: int
        :param KEYS_PRESSED: int
        :return: none
        """
        if KEYS_PRESSED[pygame.K_d] and self.getDirX() == 1:
            self.setSpeed(self.getSpeed() + 1)
            if self.getSpeed() > 5:
                self.setSpeed(5)
            self.setDirY(-1)
        elif KEYS_PRESSED[pygame.K_a] and self.getDirX() == -1:
            self.setSpeed(self.getSpeed() + 1)
            if self.getSpeed() > 5:
                self.setSpeed(5)
            self.setDirY(-1)
        elif not KEYS_PRESSED[pygame.K_a] and not KEYS_PRESSED[pygame.K_d]:
            self.setDirY(-1)
        else:
            self.setSpeed(self.getSpeed() - 1)
            if self.getSpeed() <= 1:
                self.setSpeed(2)
            self.setDirY(-1)
    def checkLostLife(self):



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

