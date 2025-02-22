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
import time

class Game:
    def __init__(self):
        # WINDOW
        self.__GAME_WINDOW = Window("Brick Breaker!")
        # LEVEL ONE BRICKS (Example of Aggregation)
        self.__BRICKLIST = []
        for i in range(6):
            ROW = []
            offset_x = 120 if i % 2 == 0 else 180  # Adjust offset_x based on i
            for j in range(6):
                ADDBRICK = Bricks()
                ADDBRICK.setDim(120, 40)
                ADDBRICK.setPOS(offset_x + j * 130, 40 + i * 50)
                ROW.append(ADDBRICK)
            self.__BRICKLIST.append(ROW)
        # PADDLE
        self.__PLAYER = Paddle(175, 8)
        self.__PLAYER.setPOS(self.__GAME_WINDOW.getWidth() // 2 - self.__PLAYER.getWidth() // 2,
                      self.__GAME_WINDOW.getHeight() // 2 - self.__PLAYER.getHeight() // 2 + 250)
        self.__PLAYER.setSpeed(7)
        # self.__BALL
        self.__BALL = Ball()
        self.__BALL.setDim(9, 9)
        self.__BALL.setPOS(self.__GAME_WINDOW.getWidth() // 2 - self.__BALL.getWidth() // 2,
                    (self.__GAME_WINDOW.getHeight() // 2 - self.__BALL.getHeight() // 2) + 100)
        self.__BALL.setSpeed(3)
        # LIFE
        self.__LIVES = 5
        self.__LIVESTEXT = Text(f"Lives: {self.__LIVES}")
        self.__LIVESTEXT.setPOS(0,0)
        self.__LIVESTEXT.setColor((63,12,249))

    def Run(self):
        """
        Runs the game.
        :return: none
        """
        # Start Screen Setup
        pygame.init()
        START_SCREEN = True
        LEVELONE = False
        LEVELTWO = False
        LEVELTHREE = False
        END_SCREEN = False
        while True:
            # Setup Stars for start screen (Aggregation)
            START_SCREEN_STARS = []
            for i in range(200):
                WIDTH = randint(3, 5)
                START_SCREEN_STARS.append(Ball(WIDTH, WIDTH))
                START_SCREEN_STARS[-1].setPOS(
                    randint(0, self.__GAME_WINDOW.getWidth() - WIDTH),
                    randint(0, self.__GAME_WINDOW.getHeight() - WIDTH)
                )
            # Setup Text class for welcome text
            START_SCREEN_WELCOME = Text("""Welcome to Brick Breaker, Press 1 To Play!;)""")
            START_SCREEN_WELCOME.setColor((173, 216, 230))
            START_SCREEN_WELCOME.setPOS(self.__GAME_WINDOW.getWidth()//2 - START_SCREEN_WELCOME.getWidth()//2, self.__GAME_WINDOW.getHeight()//2 - START_SCREEN_WELCOME.getHeight()//2)
            while START_SCREEN:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                # Inputs
                PRESSED_KEYS = pygame.key.get_pressed()
                # Processing
                for star in START_SCREEN_STARS:
                    star.WASDmove(PRESSED_KEYS)
                    star.wrapEdges(self.__GAME_WINDOW.getWidth(), self.__GAME_WINDOW.getHeight())
                # Outputs
                self.__GAME_WINDOW.clearScreen()
                for stars in START_SCREEN_STARS:
                    self.__GAME_WINDOW.getSurface().blit(stars.getSurface(), stars.getPOS())
                self.__GAME_WINDOW.getSurface().blit(START_SCREEN_WELCOME.getSurface(), START_SCREEN_WELCOME.getPOS())
                self.__GAME_WINDOW.updateFrame()
                # Checks if the user has decided to start the game
                if PRESSED_KEYS[pygame.K_1]:
                    START_SCREEN = False
                    LEVELONE = True
            # 1st Level
            while LEVELONE:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                # INPUTS
                PRESSED_KEYS = pygame.key.get_pressed()
                # PROCESSING
                ## Paddle
                self.__PLAYER.WASDmove(PRESSED_KEYS)
                self.__PLAYER.wrapEdges(self.__GAME_WINDOW.getWidth())
                ## BALL
                self.__BALL.initiateBallMove()
                self.__BALL.bounceXandY(self.__GAME_WINDOW.getWidth())
                ## BALL Collide with Paddle
                if self.__PLAYER.isCollision(self.__BALL.getSurface(), self.__BALL.getPOS()):
                    self.__BALL.collideBouncePaddle(PRESSED_KEYS)
                ## BALL collide with brick
                BRICK = self.__BALL.isCollisionBricks(self.__BRICKLIST)
                self.__BALL.CollideBounceBrick(BRICK)
                ## Lives left & resets the game
                if self.__BALL.checkLostLife(self.__GAME_WINDOW.getHeight()):
                    # Check if they still have lives left
                    if self.__LIVES <= 1:
                        LOST = Text("""Oh no! You lost""")
                        LOST.setColor((63, 12, 249))
                        LOST.setPOS(self.__GAME_WINDOW.getWidth() // 2 - LOST.getWidth() // 2,
                                    self.__GAME_WINDOW.getHeight() // 2 - LOST.getHeight() // 2)
                        self.__GAME_WINDOW.getSurface().blit(LOST.getSurface(), LOST.getPOS())
                        self.__GAME_WINDOW.updateFrame()
                        # Initiates startscreen and stops the level one while loop
                        START_SCREEN = True
                        LEVELONE = False
                        # Resets everything
                        # BALL Reset
                        self.__BALL.setPOS(self.__GAME_WINDOW.getWidth() // 2 - self.__BALL.getWidth() // 2, (self.__GAME_WINDOW.getHeight() // 2 - self.__BALL.getHeight() // 2) + 100)
                        self.__BALL.setSpeed(3)
                        # Paddle Reset
                        self.__PLAYER.setPOS(
                            self.__GAME_WINDOW.getWidth() // 2 - self.__PLAYER.getWidth() // 2,
                            self.__GAME_WINDOW.getHeight() // 2 - self.__PLAYER.getHeight() // 2 + 250
                        )
                        self.__PLAYER.setSpeed(7)
                        # Lives reset
                        self.__LIVES = 5
                        self.__LIVESTEXT = Text(f"Lives: {self.__LIVES}")
                        self.__LIVESTEXT.setColor((63, 12, 249))
                        # Reset Bricks
                        self.__BRICKLIST = []
                        for i in range(6):
                            ROW = []
                            offset_x = 120 if i % 2 == 0 else 180  # Adjust offset_x based on i
                            for j in range(6):
                                ADDBRICK = Bricks()
                                ADDBRICK.setDim(120, 40)
                                ADDBRICK.setPOS(offset_x + j * 130, 40 + i * 50)
                                ROW.append(ADDBRICK)
                            self.__BRICKLIST.append(ROW)
                        # Stops the loop, acts as a buffer
                        time.sleep(2)
                        break
                    if self.__LIVES > 1:
                        # LIVES UPDATE
                        self.__LIVES = self.__LIVES - 1
                        self.__LIVESTEXT = Text(f"Lives: {self.__LIVES}")
                        self.__LIVESTEXT.setColor((63, 12, 249))
                        # self.__BALL Reset
                        self.__BALL.setPOS(self.__GAME_WINDOW.getWidth() // 2 - self.__BALL.getWidth() // 2, (self.__GAME_WINDOW.getHeight() // 2 - self.__BALL.getHeight() // 2) + 100)
                        self.__BALL.setSpeed(3)
                        # Paddle Reset
                        self.__PLAYER.setPOS(
                            self.__GAME_WINDOW.getWidth() // 2 - self.__PLAYER.getWidth() // 2, self.__GAME_WINDOW.getHeight() // 2 - self.__PLAYER.getHeight() // 2 + 250
                        )
                        self.__PLAYER.setSpeed(7)
                # Checks if all the bricks are finished & initiates level two
                if all(not LIST for LIST in self.__BRICKLIST):
                    LEVELONE = False
                    LEVELTWO = True
                    # Reset brick formation for level 2
                    for i in range(len(self.__BRICKLIST)):
                        if i == 0 or i == 5:
                            ADDBRICK = Bricks()
                            ADDBRICK.setDim(120, 40)
                            ADDBRICK.setPOS(self.__GAME_WINDOW.getWidth() // 2 - ADDBRICK.getWidth() // 2, 40 + i * 50)
                            self.__BRICKLIST[i].append(ADDBRICK)
                        if i == 1 or i == 4:
                            for j in range(3):
                                ADDBRICK = Bricks()
                                ADDBRICK.setDim(120, 40)
                                ADDBRICK.setPOS(282.5 + 180 * (j), 40 + i * 50)
                                self.__BRICKLIST[i].append(ADDBRICK)
                        if i == 2 or i == 3:
                            for j in range(5):
                                ADDBRICK = Bricks()
                                ADDBRICK.setDim(120, 40)
                                ADDBRICK.setPOS(102.5 + 180 * (j), 40 + i * 50)
                                self.__BRICKLIST[i].append(ADDBRICK)
                    # Reset position of paddle and ball for level 2
                    # Ball
                    self.__BALL.setPOS(self.__GAME_WINDOW.getWidth() // 2 - self.__BALL.getWidth() // 2, (self.__GAME_WINDOW.getHeight() // 2 - self.__BALL.getHeight() // 2) + 100)
                    self.__BALL.setSpeed(3)
                    self.__BALL.setDirY(1)
                    # Paddle
                    self.__PLAYER.setPOS(
                        self.__GAME_WINDOW.getWidth() // 2 - self.__PLAYER.getWidth() // 2,
                        self.__GAME_WINDOW.getHeight() // 2 - self.__PLAYER.getHeight() // 2 + 250
                    )
                    self.__PLAYER.setSpeed(7)
                    break
                # OUTPUTS
                self.__GAME_WINDOW.getSurface().blit(self.__BALL.getSurface(), self.__BALL.getPOS())
                self.__GAME_WINDOW.getSurface().blit(self.__PLAYER.getSurface(), self.__PLAYER.getPOS())
                for i in range(len(self.__BRICKLIST)):
                    for j in range(len(self.__BRICKLIST[i])):
                        self.__GAME_WINDOW.getSurface().blit(self.__BRICKLIST[i][j].getSurface(), self.__BRICKLIST[i][j].getPOS())
                self.__GAME_WINDOW.getSurface().blit(self.__LIVESTEXT.getSurface(), self.__LIVESTEXT.getPOS())
                self.__GAME_WINDOW.updateFrame()
                self.__GAME_WINDOW.clearScreen()
            # 2nd LEVEL
            while LEVELTWO:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                # INPUTS
                PRESSED_KEYS = pygame.key.get_pressed()
                # PROCESSING
                ## Paddle
                self.__PLAYER.WASDmove(PRESSED_KEYS)
                self.__PLAYER.wrapEdges(self.__GAME_WINDOW.getWidth())
                ## BALL
                self.__BALL.initiateBallMove()
                self.__BALL.bounceXandY(self.__GAME_WINDOW.getWidth())
                ## BALL Collide with PLAYER
                if self.__PLAYER.isCollision(self.__BALL.getSurface(), self.__BALL.getPOS()):
                    self.__BALL.collideBouncePaddle(PRESSED_KEYS)
                ## BALL collide with brick
                BRICK = self.__BALL.isCollisionBricks(self.__BRICKLIST)
                self.__BALL.CollideBounceBrick(BRICK)
                ## Lives left & resets the game
                if self.__BALL.checkLostLife(self.__GAME_WINDOW.getHeight()):
                    # Check if they still have lives left
                    if self.__LIVES <= 1:
                        LOST = Text("""Oh no! You lost :(""")
                        LOST.setColor((63, 12, 249))
                        LOST.setPOS(self.__GAME_WINDOW.getWidth() // 2 - LOST.getWidth() // 2,
                                    self.__GAME_WINDOW.getHeight() // 2 - LOST.getHeight() // 2)
                        self.__GAME_WINDOW.getSurface().blit(LOST.getSurface(), LOST.getPOS())
                        self.__GAME_WINDOW.updateFrame()
                        # Initiates startscreen and stops the level one while loop
                        START_SCREEN = True
                        LEVELTWO = False
                        # Resets everything
                        # self.__BALL Reset
                        self.__BALL.setPOS(self.__GAME_WINDOW.getWidth() // 2 - self.__BALL.getWidth() // 2, (self.__GAME_WINDOW.getHeight() // 2 - self.__BALL.getHeight() // 2) + 100)
                        self.__BALL.setSpeed(3)
                        # Paddle Reset
                        self.__PLAYER.setPOS(
                            self.__GAME_WINDOW.getWidth() // 2 - self.__PLAYER.getWidth() // 2,
                            self.__GAME_WINDOW.getHeight() // 2 - self.__PLAYER.getHeight() // 2 + 250
                        )
                        self.__PLAYER.setSpeed(7)
                        # Lives reset
                        self.__LIVES = 5
                        self.__LIVESTEXT = Text(f"Lives: {self.__LIVES}")
                        self.__LIVESTEXT.setColor((63, 12, 249))
                        # Reset Bricks
                        self.__BRICKLIST = []
                        for i in range(6):
                            ROW = []
                            offset_x = 120 if i % 2 == 0 else 180  # Adjust offset_x based on i
                            for j in range(6):
                                ADDBRICK = Bricks()
                                ADDBRICK.setDim(120, 40)
                                ADDBRICK.setPOS(offset_x + j * 130, 40 + i * 50)
                                ROW.append(ADDBRICK)
                            self.__BRICKLIST.append(ROW)
                        # Stops the loop, acts as a buffer
                        time.sleep(2)
                        break
                    if self.__LIVES > 1:
                        # LIVES UPDATE
                        self.__LIVES = self.__LIVES - 1
                        self.__LIVESTEXT = Text(f"Lives: {self.__LIVES}")
                        self.__LIVESTEXT.setColor((63, 12, 249))
                        # BALL Reset
                        self.__BALL.setPOS(self.__GAME_WINDOW.getWidth() // 2 - self.__BALL.getWidth() // 2, (self.__GAME_WINDOW.getHeight() // 2 - self.__BALL.getHeight() // 2) + 100)
                        self.__BALL.setSpeed(3)
                        # Paddle Reset
                        self.__PLAYER.setPOS(
                            self.__GAME_WINDOW.getWidth() // 2 - self.__PLAYER.getWidth() // 2, self.__GAME_WINDOW.getHeight() // 2 - self.__PLAYER.getHeight() // 2 + 250
                        )
                        self.__PLAYER.setSpeed(7)
                if all(not OBJECT for OBJECT in self.__BRICKLIST):
                    LEVELTWO = False
                    LEVELTHREE = True
                    # Reset brick formation for level 3
                    self.__BRICKLIST = []
                    for i in range(6):
                        ROW = []
                        offset_x = 120 if i % 2 == 0 else 180  # Adjust offset_x based on i
                        for j in range(6):
                            ADDBRICK = Bricks()
                            ADDBRICK.setDim(60, 40)
                            ADDBRICK.setPOS(offset_x + j * 125, 40 + i * 45)
                            ROW.append(ADDBRICK)
                        self.__BRICKLIST.append(ROW)
                    # Reset position of paddle and ball for level 3
                    # Ball
                    self.__BALL.setPOS(self.__GAME_WINDOW.getWidth() // 2 - self.__BALL.getWidth() // 2,
                                       (self.__GAME_WINDOW.getHeight() // 2 - self.__BALL.getHeight() // 2) + 100)
                    self.__BALL.setSpeed(3)
                    self.__BALL.setDirY(1)
                    # Paddle
                    self.__PLAYER.setPOS(
                        self.__GAME_WINDOW.getWidth() // 2 - self.__PLAYER.getWidth() // 2,
                        self.__GAME_WINDOW.getHeight() // 2 - self.__PLAYER.getHeight() // 2 + 250
                    )
                    self.__PLAYER.setSpeed(7)
                    break
                # OUTPUTS
                self.__GAME_WINDOW.getSurface().blit(self.__BALL.getSurface(), self.__BALL.getPOS())
                self.__GAME_WINDOW.getSurface().blit(self.__PLAYER.getSurface(), self.__PLAYER.getPOS())
                for i in range(len(self.__BRICKLIST)):
                    for j in range(len(self.__BRICKLIST[i])):
                        self.__GAME_WINDOW.getSurface().blit(self.__BRICKLIST[i][j].getSurface(),
                                                             self.__BRICKLIST[i][j].getPOS())
                self.__GAME_WINDOW.getSurface().blit(self.__LIVESTEXT.getSurface(), self.__LIVESTEXT.getPOS())
                self.__GAME_WINDOW.updateFrame()
                self.__GAME_WINDOW.clearScreen()

            # 3rd LEVEL
            while LEVELTHREE:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                # INPUTS
                PRESSED_KEYS = pygame.key.get_pressed()
                # PROCESSING
                ## Paddle
                self.__PLAYER.WASDmove(PRESSED_KEYS)
                self.__PLAYER.wrapEdges(self.__GAME_WINDOW.getWidth())
                ## BALL
                self.__BALL.initiateBallMove()
                self.__BALL.bounceXandY(self.__GAME_WINDOW.getWidth())
                ## BALL Collide with PLAYER
                if self.__PLAYER.isCollision(self.__BALL.getSurface(), self.__BALL.getPOS()):
                    self.__BALL.collideBouncePaddle(PRESSED_KEYS)
                ## BALL collide with brick
                BRICK = self.__BALL.isCollisionBricks(self.__BRICKLIST)
                self.__BALL.CollideBounceBrick(BRICK)
                ## Lives left & resets the game
                if self.__BALL.checkLostLife(self.__GAME_WINDOW.getHeight()):
                    # Check if they still have lives left
                    if self.__LIVES <= 1:
                        LOST = Text("""Oh no! You lost :(""")
                        LOST.setColor((63, 12, 249))
                        LOST.setPOS(self.__GAME_WINDOW.getWidth() // 2 - LOST.getWidth() // 2,
                                    self.__GAME_WINDOW.getHeight() // 2 - LOST.getHeight() // 2)
                        self.__GAME_WINDOW.getSurface().blit(LOST.getSurface(), LOST.getPOS())
                        self.__GAME_WINDOW.updateFrame()
                        # Initiates startscreen and stops the level one while loop
                        START_SCREEN = True
                        LEVELTHREE = False
                        # Resets everything
                        # self.__BALL Reset
                        self.__BALL.setPOS(self.__GAME_WINDOW.getWidth() // 2 - self.__BALL.getWidth() // 2, (
                                    self.__GAME_WINDOW.getHeight() // 2 - self.__BALL.getHeight() // 2) + 100)
                        self.__BALL.setSpeed(3)
                        # Paddle Reset
                        self.__PLAYER.setPOS(
                            self.__GAME_WINDOW.getWidth() // 2 - self.__PLAYER.getWidth() // 2,
                            self.__GAME_WINDOW.getHeight() // 2 - self.__PLAYER.getHeight() // 2 + 250
                        )
                        self.__PLAYER.setSpeed(7)
                        # Lives reset
                        self.__LIVES = 5
                        self.__LIVESTEXT = Text(f"Lives: {self.__LIVES}")
                        self.__LIVESTEXT.setColor((63, 12, 249))
                        # Reset Bricks
                        self.__BRICKLIST = []
                        for i in range(6):
                            ROW = []
                            offset_x = 120 if i % 2 == 0 else 180  # Adjust offset_x based on i
                            for j in range(6):
                                ADDBRICK = Bricks()
                                ADDBRICK.setDim(120, 40)
                                ADDBRICK.setPOS(offset_x + j * 130, 40 + i * 50)
                                ROW.append(ADDBRICK)
                            self.__BRICKLIST.append(ROW)
                        # Stops the loop, acts as a buffer
                        time.sleep(2)
                        break
                    if self.__LIVES > 1:
                        # LIVES UPDATE
                        self.__LIVES = self.__LIVES - 1
                        self.__LIVESTEXT = Text(f"Lives: {self.__LIVES}")
                        self.__LIVESTEXT.setColor((63, 12, 249))
                        # BALL Reset
                        self.__BALL.setPOS(self.__GAME_WINDOW.getWidth() // 2 - self.__BALL.getWidth() // 2, (
                                    self.__GAME_WINDOW.getHeight() // 2 - self.__BALL.getHeight() // 2) + 100)
                        self.__BALL.setSpeed(3)
                        # Paddle Reset
                        self.__PLAYER.setPOS(
                            self.__GAME_WINDOW.getWidth() // 2 - self.__PLAYER.getWidth() // 2,
                            self.__GAME_WINDOW.getHeight() // 2 - self.__PLAYER.getHeight() // 2 + 250
                        )
                        self.__PLAYER.setSpeed(7)
                if all(not OBJECT for OBJECT in self.__BRICKLIST):
                    LEVELTHREE = False
                    END_SCREEN = True
                    # Reset brick formation for level 1
                    self.__BRICKLIST = []
                    for i in range(6):
                        ROW = []
                        offset_x = 120 if i % 2 == 0 else 180  # Adjust offset_x based on i
                        for j in range(6):
                            ADDBRICK = Bricks()
                            ADDBRICK.setDim(120, 40)
                            ADDBRICK.setPOS(offset_x + j * 130, 40 + i * 50)
                            ROW.append(ADDBRICK)
                        self.__BRICKLIST.append(ROW)
                    # Reset position of paddle and ball for level 1
                    # Ball
                    self.__BALL.setPOS(self.__GAME_WINDOW.getWidth() // 2 - self.__BALL.getWidth() // 2, (self.__GAME_WINDOW.getHeight() // 2 - self.__BALL.getHeight() // 2) + 100)
                    self.__BALL.setSpeed(3)
                    self.__BALL.setDirY(1)
                    # Paddle
                    self.__PLAYER.setPOS(
                        self.__GAME_WINDOW.getWidth() // 2 - self.__PLAYER.getWidth() // 2,
                        self.__GAME_WINDOW.getHeight() // 2 - self.__PLAYER.getHeight() // 2 + 250
                    )
                    self.__PLAYER.setSpeed(7)
                    break
                # OUTPUTS
                self.__GAME_WINDOW.getSurface().blit(self.__BALL.getSurface(), self.__BALL.getPOS())
                self.__GAME_WINDOW.getSurface().blit(self.__PLAYER.getSurface(), self.__PLAYER.getPOS())
                for i in range(len(self.__BRICKLIST)):
                    for j in range(len(self.__BRICKLIST[i])):
                        self.__GAME_WINDOW.getSurface().blit(self.__BRICKLIST[i][j].getSurface(),
                                                             self.__BRICKLIST[i][j].getPOS())
                self.__GAME_WINDOW.getSurface().blit(self.__LIVESTEXT.getSurface(),
                                                     self.__LIVESTEXT.getPOS())
                self.__GAME_WINDOW.updateFrame()
                self.__GAME_WINDOW.clearScreen()
            while END_SCREEN:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

                # Inputs
                PRESSED_KEYS = pygame.key.get_pressed()
                # End screen text/ Process
                ENDSCREENTEXT = Text("GOOD JOB!! YOU BEAT BRICK BREAKER! Press 2 to play again!")
                ENDSCREENTEXT.setPOS(self.__GAME_WINDOW.getWidth() // 2 - ENDSCREENTEXT.getWidth()//2, self.__GAME_WINDOW.getHeight() // 2 - ENDSCREENTEXT.getHeight() // 2)
                ENDSCREENTEXT.setColor((63, 12, 249))
                self.__GAME_WINDOW.clearScreen()
                self.__GAME_WINDOW.getSurface().blit(ENDSCREENTEXT.getSurface(), ENDSCREENTEXT.getPOS())
                self.__GAME_WINDOW.updateFrame()

                # Checks if the player decides to play again and resets their lives
                if PRESSED_KEYS[pygame.K_2]:
                    START_SCREEN = True
                    self.__LIVES = 5
                    self.__LIVESTEXT = Text(f"Lives: {self.__LIVES}")
                    self.__LIVESTEXT.setColor((63, 12, 249))
                    END_SCREEN = False











if __name__ == "__main__":
    GAME = Game()
    GAME.Run()
