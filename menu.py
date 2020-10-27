import pygame
import singletons
import effects


class _menuItem:
    def __init__(self, text, defaultColor, selectedColor, pos, description, fontSize = 48):
        font = pygame.font.Font('fonts/papercut.ttf', fontSize)
        self.__pos = pos
        self.__index = 0
        self.__description = description
        self.__items = (font.render(text, True, defaultColor),
                        font.render(text, True, selectedColor))

    def select(self):
        self.__index = 1

    def deselect(self):
        self.__index = 0

    def getItemData(self):
        return self.__items[self.__index], self.__pos

    @property
    def description(self):
        return self.__description


class Menu:
    defaultColor = (32, 68, 71)
    selectedColor = (100, 19, 16)

    def __init__(self):
        self.__items = []
        self.__display = singletons.Display().getInstance()

        self.__center_x = self.__display.getScreenResolution[0] / 2 - 100
        self.__center_y = self.__display.getScreenResolution[1] / 2 - 100

        x, y = self.__center_x, self.__center_y
        dc, sc = self.defaultColor, self.selectedColor
        self.__items.append(_menuItem('play', dc, sc, (x, y), singletons.GameMode.GAME))
        self.__items.append(_menuItem('save/load', dc, sc, (x, y + 60), singletons.GameMode.SAVE_LOAD))
        self.__items.append(_menuItem('settings', dc, sc, (x, y + 120), singletons.GameMode.SETTINGS))
        self.__items.append(_menuItem('exit', dc, sc, (x, y + 180), singletons.GameMode.EXIT))

        self.__currentIndex = 0
        self.__maxIndex = len(self.__items)
        self.__items[self.__currentIndex].select()
        self.__fire = effects.Fire((self.__center_x - 64, self.__center_y - 10))
        self.__gameMode = singletons.GameMode.getInstance()

    def update(self):
        self.__fire.update()

    def draw(self):
        for t in self.__items:
            text, pos = t.getItemData()
            self.__display.getSurface.blit(text, pos)

        self.__fire.draw()

    def eventProcessing(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                self.__items[self.__currentIndex].deselect()
                self.__currentIndex += 1
                if self.__currentIndex >= self.__maxIndex:
                    self.__currentIndex = 0
                self.__items[self.__currentIndex].select()
                self.__fire.setPosition((self.__center_x - 64, self.__center_y - 10 + 60 * self.__currentIndex))
            elif event.key == pygame.K_UP:
                self.__items[self.__currentIndex].deselect()
                self.__currentIndex -= 1
                if self.__currentIndex < 0:
                    self.__currentIndex = self.__maxIndex - 1
                self.__items[self.__currentIndex].select()
                self.__fire.setPosition((self.__center_x - 64, self.__center_y - 10 + 60 * self.__currentIndex))
            elif event.key == pygame.K_RETURN:
                if self.__items[self.__currentIndex].description == singletons.GameMode.GAME:
                    self.__gameMode.setGame()



