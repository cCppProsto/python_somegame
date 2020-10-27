import pygame


class Display:
    __instance = None

    # 31 x 20
    __SCREEN_RESOLUTION = (992, 640)  # type: tuple(int, int)
    __BG_COLOR = (0, 0, 0)
    __FPS = 30

    def __init__(self):
        self.__surface = None

    def init(self):
        if self.__surface is None:
            self.__surface = pygame.display.set_mode(self.__SCREEN_RESOLUTION)

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = Display()
        return cls.__instance

    @property
    def getScreenResolution(self):
        return self.__SCREEN_RESOLUTION

    @property
    def getBGColor(self):
        return self.__BG_COLOR

    @property
    def getFPS(self):
        return self.__FPS

    @property
    def getSurface(self):
        return self.__surface


class GameMode:
    MENU = 'menu'
    GAME = 'game'
    PAUSE = 'pause'
    SAVE_LOAD = 'save_load'
    SETTINGS = 'settings'
    EXIT = 'exit'

    __instance = None

    def __init__(self):
        self.__currentState = self.MENU

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = GameMode()
        return cls.__instance

    @property
    def state(self):
        return self.__currentState

    def setMenu(self):
        self.__currentState = self.MENU

    def setGame(self):
        self.__currentState = self.GAME

    def setPause(self):
        self.__currentState = self.PAUSE

    def setSettings(self):
        self.__currentState = self.SETTINGS

    def setExit(self):
        self.__currentState = self.EXIT
