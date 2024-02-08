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
