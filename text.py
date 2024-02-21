'''
Title: Text class inheriting from box class
author: Sean Jin
date-created: 20-02-2024
'''

from box import Box
import pygame

class Text(Box):
    def __init__(self, TEXT, F_FAMILY="Times New Roman", F_SIZE=36):
        Box.__init__(self)
        self.__TEXT = TEXT
        self.__FONT_FAMILY = F_FAMILY
        self.__FONT_SIZE = F_SIZE
        self.__FONT = pygame.font.SysFont(self.__FONT_FAMILY, self.__FONT_SIZE)
        self._SURFACE = self.__FONT.render(self.__TEXT, True, self._COLOR)

    def setColor(self, TUPLE):
        Box.setColor(self, TUPLE)
        self._SURFACE = self.__FONT.render(self.__TEXT, True, self._COLOR)

if __name__ == "__main__":
    from Window import Window
    pygame.init()

    WINDOW = Window("Text subClass")
    TEXT = Text("Hello World")
    TEXT.setColor((0,255,0))
    TEXT.setPOS(WINDOW.getWidth()//2 - TEXT.getWidth()//2, WINDOW.getHeight()//2 - TEXT.getHeight()//2)
    print(TEXT.getPOS())
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


        WINDOW.clearScreen()
        WINDOW.getSurface().blit(TEXT.getSurface(), TEXT.getPOS())
        WINDOW.updateFrame()
