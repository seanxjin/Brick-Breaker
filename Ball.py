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
        :param KEYS_PRESSED: int
        :return: none
        """
        if KEYS_PRESSED[pygame.K_d] and self.getDirX() == 1:
            self.setSpeed(self.getSpeed() + 0.5)
            if self.getSpeed() > 5:
                self.setSpeed(5)
            self.setDirY(-1)
        elif KEYS_PRESSED[pygame.K_a] and self.getDirX() == -1:
            self.setSpeed(self.getSpeed() + 0.5)
            if self.getSpeed() > 5:
                self.setSpeed(5)
            self.setDirY(-1)
        elif not KEYS_PRESSED[pygame.K_a] and not KEYS_PRESSED[pygame.K_d]:
            self.setDirY(-1)
        else:
            self.setSpeed(self.getSpeed() - 0.5)
            if self.getSpeed() <= 1:
                self.setSpeed(2)
            self.setDirY(-1)
    def isCollisionBricks(self, BRICKLIST):
        """
        Boolean function that checks if a current sprites position is overlapping with another sprite
        :param BRICKLIST: 2d array -> list -> object
        :return: int
        """
        # Only checks if the 2 sprites collide with one another
        for i in range(len(BRICKLIST)):
            for j in range(len(BRICKLIST[i])-1,-1,-1):
                WIDTH = BRICKLIST[i][j].getWidth()
                HEIGHT = BRICKLIST[i][j].getHeight()
                X = BRICKLIST[i][j].getX()
                Y = BRICKLIST[i][j].getY()
                if X >= self.getX() - WIDTH and X <= self.getX() + self.getWidth():
                    if Y >= self.getY() - HEIGHT and Y <= self.getY() + self.getHeight():
                        BRICKLIST[i].pop(j)
                        # Checks which side the sprites collide on
                        OVERLAP_LEFT = abs((self.getX() - WIDTH) - X) # Closest to the left side
                        OVERLAP_RIGHT = abs((self.getX() + self.getWidth()) - X) # Closest to the right side
                        OVERLAP_TOP = abs((self.getY() - HEIGHT) - Y) # Closest to the top side
                        OVERLAP_BOTTOM = abs((self.getY() + self.getHeight()) - Y) # Closest to the bottom side
                        # Checks the smallest value/distance between the sides to determine which side it hits
                        MIN_OVERLAP = min(OVERLAP_LEFT, OVERLAP_RIGHT, OVERLAP_TOP, OVERLAP_BOTTOM)
                        if MIN_OVERLAP == OVERLAP_LEFT or MIN_OVERLAP == OVERLAP_RIGHT:
                            return 1
                        elif MIN_OVERLAP == OVERLAP_TOP or MIN_OVERLAP == OVERLAP_BOTTOM:
                            return 2

                        else:
                            pass
                    else:
                        pass
    def CollideBounceBrick(self, SIDE):
        """
        How the ball behaves when bouncing with a brick
        :param SIDE: int
        :return: none
        """
        if SIDE == 1:
            self.setDirX(self.getDirX()*-1)
        elif SIDE == 2:
            self.setDirY(self.getDirY()*-1)

    def checkLostLife(self, MAX_HEIGHT):
        """
        Checks the Y position of the ball, if it goes out of bounds it returns true.
        :param MAX_HEIGHT: int
        :return: bool
        """
        if self.getY() > MAX_HEIGHT - self.getHeight():
            return True
        else:
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

