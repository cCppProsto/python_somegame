import pygame
import singletons


class Fire(pygame.sprite.Sprite):
    def __init__(self, pos=(0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.spriteCount = 0
        self.image = None
        self.fpsIndex = 0
        self.step = 0
        self.indexResetValue = 0
        self.loadSprites()
        self.__pos = pos
        self.__surface = singletons.Display().getInstance().getSurface

    def loadSprites(self):
        path = 'assets/effects/fire/'
        for i in range(1, 60):
            self.images.append(pygame.image.load(path + str(i) + '.png'))

        self._updateIndexes()

    def update(self, *args):
        self.image = self.images[self.fpsIndex / self.step]
        self.fpsIndex += 1
        if self.fpsIndex >= self.indexResetValue:
            self.fpsIndex = 0

    def _updateIndexes(self):
        self.spriteCount = len(self.images)
        self.image = self.images[0]
        self.fpsIndex = 0
        self.step = 60 / self.spriteCount
        self.indexResetValue = self.step * self.spriteCount

    def setPosition(self, pos):
        self.__pos = pos

    def draw(self):
        self.__surface.blit(self.image, self.__pos)
