'''
title: Game class
author: Sean Jin
date-created: 07-02-2024
'''

import pygame
from box import Box
from Window import Window
from paddle import Paddle
from Ball import Ball
from bricks import Bricks
from random import randint

class Game:
    def __init__(self):
        self.__BRICKLIST = []
        for i in range(6):
            ROW = []
            offset_x = 120 if i % 2 == 0 else 180  # Adjust offset_x based on i
            for j in range(6):
                ADDBRICK = Bricks()
                ADDBRICK.setDim(120, 40)
                ADDBRICK.setPOS(offset_x + j * 125, 40 + i * 45)
                ROW.append(ADDBRICK)
            self.__BRICKLIST.append(ROW)
        self.__PLAYER = Paddle()
        self.__BALL = Ball()
        self.__LIFE = 3

    def Run(self):
        """
        Runs the game.
        :return: none
        """
        pass


if __name__ == "__main__":
    pygame.init()
    GAME_WINDOW = Window("Brick Breaker!")
    START_SCREEN_STARS = []
    for i in range(200):
        WIDTH = randint(3, 5)
        START_SCREEN_STARS.append(Ball(WIDTH, WIDTH))
        START_SCREEN_STARS[-1].setPOS(
            randint(0, GAME_WINDOW.getWidth() - WIDTH),
            randint(0, GAME_WINDOW.getHeight() - WIDTH)
        )
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        PRESSED_KEYS = pygame.key.get_pressed()

        for star in START_SCREEN_STARS:
            star.WASDmove(PRESSED_KEYS)

        GAME_WINDOW.clearScreen()
        for stars in START_SCREEN_STARS:
            GAME_WINDOW.getSurface().blit(stars.getSurface(), stars.getPOS())
        GAME_WINDOW.updateFrame()
