'''
title: Game class
author: Sean Jin
date-created: 07-02-2024
'''

import pygame
from Window import Window
from paddle import Paddle
from Ball import Ball
from bricks import Bricks
from random import randint
from text import Text

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
        # Start Screen Setup
        pygame.init()
        # Setup Window Class
        GAME_WINDOW = Window("Brick Breaker!")
        # Setup Stars for start screen
        START_SCREEN_STARS = []
        for i in range(200):
            WIDTH = randint(3, 5)
            START_SCREEN_STARS.append(Ball(WIDTH, WIDTH))
            START_SCREEN_STARS[-1].setPOS(
                randint(0, GAME_WINDOW.getWidth() - WIDTH),
                randint(0, GAME_WINDOW.getHeight() - WIDTH)
            )
        # Setup Text class for welcome text
        START_SCREEN_WELCOME = Text("""Welcome to Brick Breaker, Press 1 To Play!;)""")
        START_SCREEN_WELCOME.setColor((173, 216, 230))
        START_SCREEN_WELCOME.setPOS(GAME_WINDOW.getWidth()//2 - START_SCREEN_WELCOME.getWidth()//2, GAME_WINDOW.getHeight()//2 - START_SCREEN_WELCOME.getHeight()//2)
        # Setup ball
        BALL = Ball()
        BALL.setDim(5, 5)
        BALL.setPOS(GAME_WINDOW.getWidth() // 2 - BALL.getWidth() // 2, (GAME_WINDOW.getHeight() // 2 - BALL.getHeight() // 2) + 100)
        BALL.setSpeed(3)
        # Setup bricks
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
        # Setup Paddle
        PADDLE = Paddle(100, 8)
        PADDLE.setPOS(GAME_WINDOW.getWidth() // 2 - PADDLE.getWidth() // 2,
                      GAME_WINDOW.getHeight() // 2 - PADDLE.getHeight() // 2 + 250)
        PADDLE.setSpeed(7)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            # Inputs
            PRESSED_KEYS = pygame.key.get_pressed()
            # Processing
            for star in START_SCREEN_STARS:
                star.WASDmove(PRESSED_KEYS)
                star.wrapEdges(GAME_WINDOW.getWidth(), GAME_WINDOW.getHeight())
            # Outputs
            GAME_WINDOW.clearScreen()
            for stars in START_SCREEN_STARS:
                GAME_WINDOW.getSurface().blit(stars.getSurface(), stars.getPOS())
            GAME_WINDOW.getSurface().blit(START_SCREEN_WELCOME.getSurface(), START_SCREEN_WELCOME.getPOS())
            GAME_WINDOW.updateFrame()
            # Checks if the user has decided to start the game
            if PRESSED_KEYS[pygame.K_1]:
                break
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            # INPUTS
            PRESSED_KEYS = pygame.key.get_pressed()
            # PROCESSING
            PADDLE.WASDmove(PRESSED_KEYS)
            PADDLE.checkBoundaries(GAME_WINDOW.getWidth())
            BALL.bounceXandY(GAME_WINDOW.getWidth(), GAME_WINDOW.getHeight())
            # OUTPUTS
            GAME_WINDOW.clearScreen()
            GAME_WINDOW.getSurface().blit(BALL.getSurface(), BALL.getPOS())
            GAME_WINDOW.getSurface().blit(PADDLE.getSurface(), PADDLE.getPOS())
            for i in range(len(BRICKLIST)):
                for j in range(len(BRICKLIST[i])):
                    GAME_WINDOW.getSurface().blit(BRICKLIST[i][j].getSurface(), BRICKLIST[i][j].getPOS())
            GAME_WINDOW
            GAME_WINDOW.updateFrame()






if __name__ == "__main__":
    GAME = Game()
    GAME.Run()
