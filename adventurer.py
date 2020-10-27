import pygame
import singletons

# https://rvros.itch.io/animated-pixel-hero?download

# x = 8
# y = 5
# w = 32
# h = 32


class _BaseMode(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.spriteCount = 0
        self.image = None
        self.fpsIndex = 0
        self.step = 0
        self.indexResetValue = 0
        self.rect = None
        self.loadSprites()

    def loadSprites(self):
        pass

    def update(self, *args):
        self.image = self.images[self.fpsIndex / self.step]
        self.fpsIndex += 1
        if self.fpsIndex >= self.indexResetValue:
            self.fpsIndex = 0

    def _updateIndexes(self):
        self.spriteCount = len(self.images)
        self.image = self.images[0]
        self.fpsIndex = 0
        self.step = 30 / self.spriteCount
        self.indexResetValue = self.step * self.spriteCount
        self.size = self.images[0].get_size()


class _IdleMode(_BaseMode):
    def __init__(self):
        _BaseMode.__init__(self)

    def loadSprites(self):
        self.images.append(pygame.image.load('assets/adventurer/idle/0.png'))
        self.images.append(pygame.image.load('assets/adventurer/idle/1.png'))
        self.images.append(pygame.image.load('assets/adventurer/idle/2.png'))
        self.images.append(pygame.image.load('assets/adventurer/idle/3.png'))
        _BaseMode._updateIndexes(self)


class _RunMode(_BaseMode):
    def __init__(self):
        _BaseMode.__init__(self)

    def loadSprites(self):
        self.images.append(pygame.image.load('assets/adventurer/run/0.png'))
        self.images.append(pygame.image.load('assets/adventurer/run/1.png'))
        self.images.append(pygame.image.load('assets/adventurer/run/2.png'))
        self.images.append(pygame.image.load('assets/adventurer/run/3.png'))
        self.images.append(pygame.image.load('assets/adventurer/run/4.png'))
        self.images.append(pygame.image.load('assets/adventurer/run/5.png'))
        _BaseMode._updateIndexes(self)


class _FallingMode(_BaseMode):
    def __init__(self):
        _BaseMode.__init__(self)

    def loadSprites(self):
        self.images.append(pygame.image.load('assets/adventurer/fall/1.png'))
        self.images.append(pygame.image.load('assets/adventurer/fall/2.png'))
        _BaseMode._updateIndexes(self)


class _Animations:
    IDLE = 1
    FALL = 2
    MOVING = 3

    def __init__(self):
        self._modeIndex = self.IDLE
        self._modes = {
            self.IDLE: _IdleMode(),
            self.FALL: _FallingMode(),
            self.MOVING: _RunMode(),
        }

    def setIdle(self):
        self._modeIndex = self.IDLE

    def setFall(self):
        self._modeIndex = self.FALL

    def setMoving(self):
        self._modeIndex = self.MOVING

    @property
    def animation(self):
        return self._modes[self._modeIndex]


class Adventurer:
    IDLE = 1
    MOVE_LEFT = 2
    MOVE_RIGHT = 3
    FALLING = 4

    def __init__(self):
        self._state = self.IDLE
        self.__x = 64
        self.__y = 192
        self.__dx = 0
        self.__dy = 0
        self.__speedX = 2
        self.__speedY = 2
        self.__keyRightPressed = False
        self.__keyLeftPressed = False
        self.__isFalling = False
        self.__direction = 'Right'
        self.__animations = _Animations()
        self.__level = None
        self.__surface = singletons.Display.getInstance().getSurface
        self.__gameMode = singletons.GameMode.getInstance()

    def setLevelObject(self, level):
        self.__level = level

    def draw(self):
        if self.__direction == 'Right':
            self.__surface.blit(self.animation.image, self.position)
        else:
            self.__surface.blit(pygame.transform.flip(self.animation.image, True, False), self.position)

    def eventProcessing(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.__keyRightPressed = True
            elif event.key == pygame.K_LEFT:
                self.__keyLeftPressed = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.__keyRightPressed = False
            elif event.key == pygame.K_LEFT:
                self.__keyLeftPressed = False
            elif event.key == pygame.K_ESCAPE:
                self.__gameMode.setPause()

    def update(self):
        self.__dx = 0
        self.__dy = 0

        self.__isFalling = self.canFalling()

        if self.__keyLeftPressed:
            self.setStateMoveLeft()
        elif self.__keyRightPressed:
            self.setStateMoveRight()
        else:
            self.setStateIdle()

        self.stateProcessing()
        self.animation.update()

    def stateProcessing(self):
        if self.__isFalling:
            self.moveByDxDy(dy=self.__speedY)

        if self._state == self.MOVE_LEFT:
            if self.canMove():
                self.moveByDxDy(dx=-self.__speedX)
        elif self._state == self.MOVE_RIGHT:
            if self.canMove():
                self.moveByDxDy(dx=self.__speedX)

    def setStateMoveLeft(self):
        self.__direction = 'Left'
        self._state = self.MOVE_LEFT
        if self.__isFalling:
            self.__animations.setFall()
        else:
            self.__animations.setMoving()

    def setStateMoveRight(self):
        self.__direction = 'Right'
        self._state = self.MOVE_RIGHT
        if self.__isFalling:
            self.__animations.setFall()
        else:
            self.__animations.setMoving()

    def setStateIdle(self):
        self._state = self.IDLE
        if self.__isFalling:
            self.__animations.setFall()
        else:
            self.__animations.setIdle()

    def canMove(self):
        if self.__direction == 'Left':
            x = self.__x - self.__speedX
            cell = x / 32
            ci = cell - 1 if cell > 0 else 0
        else:
            x = self.__x + self.__speedX
            cell = x / 32
            ci = cell + 1 if cell < 30 else 30

        size = self.animation.size
        rect = pygame.Rect(x, self.__y, size[0], size[1])

        row = self.__y / 32
        c1 = self.__level.map()[row][cell]
        c2 = self.__level.map()[row][ci]
        c3 = self.__level.map()[row + 1][cell]
        c4 = self.__level.map()[row + 1][ci]
        if not (rect.colliderect(c1.rect) or
                rect.colliderect(c2.rect) or
                rect.colliderect(c3.rect) or
                rect.colliderect(c4.rect)):
            return True
        return False

    def canFalling(self):
        size = self.animation.size
        y = self.__y + self.__speedY
        row = y / 32
        cell = self.__x / 32
        rect = pygame.Rect(self.__x, y, size[0], size[1])

        ci2 = cell + 1 if cell < 30 else 30
        c1 = self.__level.map()[row][cell]
        c2 = self.__level.map()[row + 1][cell]
        c3 = self.__level.map()[row + 1][ci2]
        if not (rect.colliderect(c1.rect) or
                rect.colliderect(c2.rect) or
                rect.colliderect(c3.rect)):
            return True
        return False

    def moveByDxDy(self, dx=0, dy=0):
        self.__x += dx
        self.__y += dy

    @property
    def rect(self):
        return self.__rect

    @property
    def animation(self):
        return self.__animations.animation

    @property
    def position(self):
        return self.__x, self.__y
