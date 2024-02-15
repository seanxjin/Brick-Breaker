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

        pygame.init()
        GAME_WINDOW = Window("Brick Breaker!")
        START_SCREEN_STARS = []
        for i in range(100):
            WIDTH = randint(2,4)
            START_SCREEN_STARS.append(Box(WIDTH, WIDTH))
            START_SCREEN_STARS[-1].setPOS(
                randint(0,GAME_WINDOW.getWidth() - WIDTH),
                randint(0,GAME_WINDOW.getHeight() - WIDTH)
            )
        while True:
            for event in event.type.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            PRESSED_KEYS = pygame.key.get_pressed()

            for i in range(len(START_SCREEN_STARS)):
                START_SCREEN_STARS[i].WASDmove(PRESSED_KEYS)
            GAME_WINDOW.clearScreen()
