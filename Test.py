WIN = Text("You won!!! Congrats! Press any key to continue!")
                    WIN.setColor((63, 12, 249))
                    WIN.setPOS(self.__GAME_WINDOW.getWidth() // 2 - WIN.getWidth() // 2,
                                self.__GAME_WINDOW.getHeight() // 2 - WIN.getHeight() // 2)
                    self.__GAME_WINDOW.getSurface().blit(WIN.getSurface(), WIN.getPOS())
                    self.__GAME_WINDOW.updateFrame()