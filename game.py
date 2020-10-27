import pygame
import singletons
import adventurer
import level_1


class Game:
    def __init__(self):
        self.__adventurer = adventurer.Adventurer()
        self.__levels = []
        self.__levels.append(level_1.Level1())
        self.__levelIndex = 0
        self.__adventurer.setLevelObject(self.__levels[self.__levelIndex])

    def draw(self):
        self.__levels[self.__levelIndex].draw()
        self.__adventurer.draw()

    def eventProcessing(self, event):
        self.__adventurer.eventProcessing(event)
        self.__levels[self.__levelIndex].eventProcessing(event)

    def update(self):
        self.__adventurer.update()
        self.__levels[self.__levelIndex].update()
