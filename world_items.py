import pygame
import singletons


class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self._surface = singletons.Display.getInstance().getSurface
        self._image = pygame.image.load('assets/background.png')

    def draw(self):
        self._surface.blit(self._image, (0, 0))


class BaseItem(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self._x = x
        self._y = y
        self._rect = pygame.Rect(-1, -1, 0, 0)
        self._images = []
        self._image = None
        self._indexImage = 0
        self._surface = singletons.Display.getInstance().getSurface

    def draw(self):
        self._surface.blit(self._image, (self._x, self._y))

    def update(self, *args):
        pass

    @property
    def rect(self):
        return self._rect

    def _finishSpriteLoading(self):
        self._image = self._images[0]
        size = self._image.get_size()
        self._rect = pygame.Rect((self._x, self._y, size[0], size[1]))


class AnimateBaseItem(BaseItem):
    def __init__(self, x=0, y=0):
        BaseItem.__init__(self, x, y)
        self._spriteCount = 0
        self._fpsIndex = 0
        self._step = 0
        self._indexResetValue = 0
        self.loadSprites()

    def update(self, *args):
        self._image = self._images[self._fpsIndex / self._step]
        self._fpsIndex += 1
        if self._fpsIndex >= self._indexResetValue:
            self._fpsIndex = 0

    @property
    def __getPos(self):
        return self._x, self._y

    def _updateIndexes(self):
        self._spriteCount = len(self._images)
        self._image = self._images[0]
        self._fpsIndex = 0
        self._step = 30 / self._spriteCount
        self._indexResetValue = self._step * self._spriteCount
        size = self._image.get_size()
        self._rect = pygame.Rect((self._x, self._y, size[0], size[1]))


class Empty(BaseItem):
    def __init__(self, x=0, y=0):
        BaseItem.__init__(self, x, y)

    def draw(self):
        pass


class PlatformLong(BaseItem):
    def __init__(self, x=0, y=0):
        BaseItem.__init__(self, x, y)
        self._images.append(pygame.image.load('assets/world/static/platform-long.png'))
        self._finishSpriteLoading()


class LeftWallBorderP1(BaseItem):
    def __init__(self, x=0, y=0):
        BaseItem.__init__(self, x, y)
        self._images.append(pygame.image.load('assets/world/static/left_wall_border_1.png'))
        self._finishSpriteLoading()

class LeftWallBorderP2(BaseItem):
    def __init__(self, x=0, y=0):
        BaseItem.__init__(self, x, y)
        self._images.append(pygame.image.load('assets/world/static/left_wall_border_2.png'))
        self._finishSpriteLoading()


class LeftWallBorderP3(BaseItem):
    def __init__(self, x=0, y=0):
        BaseItem.__init__(self, x, y)
        self._images.append(pygame.image.load('assets/world/static/left_wall_border_3.png'))
        self._finishSpriteLoading()


class LeftWallBorderP4(BaseItem):
    def __init__(self, x=0, y=0):
        BaseItem.__init__(self, x, y)
        self._images.append(pygame.image.load('assets/world/static/left_wall_border_4.png'))
        self._finishSpriteLoading()


class LeftWallBorderDown(BaseItem):
    def __init__(self, x=0, y=0):
        BaseItem.__init__(self, x, y)
        self._images.append(pygame.image.load('assets/world/static/left_wall_border_down.png'))
        self._finishSpriteLoading()


class BottomWallBorder1(BaseItem):
    def __init__(self, x=0, y=0):
        BaseItem.__init__(self, x, y)
        self._images.append(pygame.image.load('assets/world/static/bottom_wall_border_1.png'))
        self._finishSpriteLoading()


class BottomWallBorder2(BaseItem):
    def __init__(self, x=0, y=0):
        BaseItem.__init__(self, x, y)
        self._images.append(pygame.image.load('assets/world/static/bottom_wall_border_2.png'))
        self._finishSpriteLoading()


class BottomWallBorder3(BaseItem):
    def __init__(self, x=0, y=0):
        BaseItem.__init__(self, x, y)
        self._images.append(pygame.image.load('assets/world/static/bottom_wall_border_3.png'))
        self._finishSpriteLoading()


class BottomWallBorder4(BaseItem):
    def __init__(self, x=0, y=0):
        BaseItem.__init__(self, x, y)
        self._images.append(pygame.image.load('assets/world/static/bottom_wall_border_4.png'))
        self._finishSpriteLoading()


class BottomWallBorder5(BaseItem):
    def __init__(self, x=0, y=0):
        BaseItem.__init__(self, x, y)
        self._images.append(pygame.image.load('assets/world/static/bottom_wall_border_5.png'))
        self._finishSpriteLoading()


class BottomWallBorder6(BaseItem):
    def __init__(self, x=0, y=0):
        BaseItem.__init__(self, x, y)
        self._images.append(pygame.image.load('assets/world/static/bottom_wall_border_6.png'))
        self._finishSpriteLoading()


class BottomWallBorder7(BaseItem):
    def __init__(self, x=0, y=0):
        BaseItem.__init__(self, x, y)
        self._images.append(pygame.image.load('assets/world/static/bottom_wall_border_7.png'))
        self._finishSpriteLoading()


class BottomWallBorder8(BaseItem):
    def __init__(self, x=0, y=0):
        BaseItem.__init__(self, x, y)
        self._images.append(pygame.image.load('assets/world/static/bottom_wall_border_8.png'))
        self._finishSpriteLoading()


class RightWallBorderDown(BaseItem):
    def __init__(self, x=0, y=0):
        BaseItem.__init__(self, x, y)
        self._images.append(pygame.image.load('assets/world/static/right_wall_border_down.png'))
        self._finishSpriteLoading()


class RightWallBorder1(BaseItem):
    def __init__(self, x=0, y=0):
        BaseItem.__init__(self, x, y)
        self._images.append(pygame.image.load('assets/world/static/right_wall_border_1.png'))
        self._finishSpriteLoading()


class RightWallBorder2(BaseItem):
    def __init__(self, x=0, y=0):
        BaseItem.__init__(self, x, y)
        self._images.append(pygame.image.load('assets/world/static/right_wall_border_2.png'))
        self._finishSpriteLoading()


class RightWallBorder3(BaseItem):
    def __init__(self, x=0, y=0):
        BaseItem.__init__(self, x, y)
        self._images.append(pygame.image.load('assets/world/static/right_wall_border_3.png'))
        self._finishSpriteLoading()


class RightWallBorder4(BaseItem):
    def __init__(self, x=0, y=0):
        BaseItem.__init__(self, x, y)
        self._images.append(pygame.image.load('assets/world/static/right_wall_border_4.png'))
        self._finishSpriteLoading()


class RightTopWallBorder1(BaseItem):
    def __init__(self, x=0, y=0):
        BaseItem.__init__(self, x, y)
        self._images.append(pygame.image.load('assets/world/static/right_top_wall_border_1.png'))
        self._finishSpriteLoading()


class RightTopWallBorder2(BaseItem):
    def __init__(self, x=0, y=0):
        BaseItem.__init__(self, x, y)
        self._images.append(pygame.image.load('assets/world/static/right_top_wall_border_2.png'))
        self._finishSpriteLoading()


class RightTopWallBorder3(BaseItem):
    def __init__(self, x=0, y=0):
        BaseItem.__init__(self, x, y)
        self._images.append(pygame.image.load('assets/world/static/right_top_wall_border_3.png'))
        self._finishSpriteLoading()


class RightTopWallBorder4(BaseItem):
    def __init__(self, x=0, y=0):
        BaseItem.__init__(self, x, y)
        self._images.append(pygame.image.load('assets/world/static/right_top_wall_border_4.png'))
        self._finishSpriteLoading()


class LeftTopWallBorder1(BaseItem):
    def __init__(self, x=0, y=0):
        BaseItem.__init__(self, x, y)
        self._images.append(pygame.image.load('assets/world/static/left_top_wall_border_1.png'))
        self._finishSpriteLoading()


class LeftTopWallBorder2(BaseItem):
    def __init__(self, x=0, y=0):
        BaseItem.__init__(self, x, y)
        self._images.append(pygame.image.load('assets/world/static/left_top_wall_border_2.png'))
        self._finishSpriteLoading()


class LeftTopWallBorder3(BaseItem):
    def __init__(self, x=0, y=0):
        BaseItem.__init__(self, x, y)
        self._images.append(pygame.image.load('assets/world/static/left_top_wall_border_3.png'))
        self._finishSpriteLoading()


class LeftTopWallBorder4(BaseItem):
    def __init__(self, x=0, y=0):
        BaseItem.__init__(self, x, y)
        self._images.append(pygame.image.load('assets/world/static/left_top_wall_border_4.png'))
        self._finishSpriteLoading()


class TopWallBorder1(BaseItem):
    def __init__(self, x=0, y=0):
        BaseItem.__init__(self, x, y)
        self._images.append(pygame.image.load('assets/world/static/top_wall_border_1.png'))
        self._finishSpriteLoading()


class TopWallBorder2(BaseItem):
    def __init__(self, x=0, y=0):
        BaseItem.__init__(self, x, y)
        self._images.append(pygame.image.load('assets/world/static/top_wall_border_2.png'))
        self._finishSpriteLoading()


class TopWallBorder3(BaseItem):
    def __init__(self, x=0, y=0):
        BaseItem.__init__(self, x, y)
        self._images.append(pygame.image.load('assets/world/static/top_wall_border_3.png'))
        self._finishSpriteLoading()


class TopWallBorder4(BaseItem):
    def __init__(self, x=0, y=0):
        BaseItem.__init__(self, x, y)
        self._images.append(pygame.image.load('assets/world/static/top_wall_border_4.png'))
        self._finishSpriteLoading()


class TopWallBorder5(BaseItem):
    def __init__(self, x=0, y=0):
        BaseItem.__init__(self, x, y)
        self._images.append(pygame.image.load('assets/world/static/top_wall_border_5.png'))
        self._finishSpriteLoading()


class BigCrate(BaseItem):
    def __init__(self, x=0, y=0):
        BaseItem.__init__(self, x, y)
        self._images.append(pygame.image.load('assets/world/static/big-crate.png'))
        self._finishSpriteLoading()


class Door(BaseItem):
    def __init__(self, x=0, y=0):
        BaseItem.__init__(self, x, y)
        self._images.append(pygame.image.load('assets/world/static/door.png'))
        self._finishSpriteLoading()


class BottomWallBorderAnim1(AnimateBaseItem):
    def __init__(self, x, y):
        AnimateBaseItem.__init__(self, x, y)

    def loadSprites(self):
        self._images.append(pygame.image.load('assets/world/static/bottom_wall_border_1_anim/bottom_wall_border_1.png'))
        self._images.append(pygame.image.load('assets/world/static/bottom_wall_border_1_anim/bottom_wall_border_2.png'))
        self._images.append(pygame.image.load('assets/world/static/bottom_wall_border_1_anim/bottom_wall_border_3.png'))
        self._images.append(pygame.image.load('assets/world/static/bottom_wall_border_1_anim/bottom_wall_border_4.png'))
        self._images.append(pygame.image.load('assets/world/static/bottom_wall_border_1_anim/bottom_wall_border_5.png'))
        self._images.append(pygame.image.load('assets/world/static/bottom_wall_border_1_anim/bottom_wall_border_6.png'))
        self._images.append(pygame.image.load('assets/world/static/bottom_wall_border_1_anim/bottom_wall_border_7.png'))
        self._images.append(pygame.image.load('assets/world/static/bottom_wall_border_1_anim/bottom_wall_border_8.png'))
        self._images.append(pygame.image.load('assets/world/static/bottom_wall_border_1_anim/bottom_wall_border_9.png'))
        self._updateIndexes()


class WallTorch(AnimateBaseItem):
    def __init__(self, x, y):
        AnimateBaseItem.__init__(self, x, y)

    def loadSprites(self):
        self._images.append(pygame.image.load('assets/items/wall_torch/0.png'))
        self._images.append(pygame.image.load('assets/items/wall_torch/1.png'))
        self._images.append(pygame.image.load('assets/items/wall_torch/2.png'))
        self._images.append(pygame.image.load('assets/items/wall_torch/3.png'))
        self._images.append(pygame.image.load('assets/items/wall_torch/4.png'))
        self._images.append(pygame.image.load('assets/items/wall_torch/5.png'))
        self._images.append(pygame.image.load('assets/items/wall_torch/6.png'))
        self._images.append(pygame.image.load('assets/items/wall_torch/7.png'))
        self._images.append(pygame.image.load('assets/items/wall_torch/8.png'))
        self._images.append(pygame.image.load('assets/items/wall_torch/9.png'))
        self._updateIndexes()


class Lights(AnimateBaseItem):
    def __init__(self, x, y):
        AnimateBaseItem.__init__(self, x, y)

    def loadSprites(self):
        self._images.append(pygame.image.load('assets/items/lights/1.png'))
        self._images.append(pygame.image.load('assets/items/lights/2.png'))
        self._images.append(pygame.image.load('assets/items/lights/3.png'))
        self._images.append(pygame.image.load('assets/items/lights/4.png'))
        self._updateIndexes()
