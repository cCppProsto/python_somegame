import pygame
import singletons
import menu
import game


def main():
    pygame.init()

    Display = singletons.Display().getInstance()
    Display.init()

    Menu = menu.Menu()
    GameMode = singletons.GameMode().getInstance()

    Game = game.Game()

    done = False
    clock = pygame.time.Clock()
    while not done:
        Display.getSurface.fill(Display.getBGColor)
        events = pygame.event.get()

        # get input data
        for event in events:
            if GameMode.state == singletons.GameMode.MENU:
                Menu.eventProcessing(event)
            elif GameMode.state == singletons.GameMode.GAME:
                Game.eventProcessing(event)
            elif GameMode.state == singletons.GameMode.PAUSE:
                pass
            elif GameMode.state == singletons.GameMode.SETTINGS:
                pass
            elif GameMode.state == singletons.GameMode.EXIT:
                pass

            if event.type == pygame.QUIT:
                done = True

        # processing
        # redraw screen
        if GameMode.state == singletons.GameMode.MENU:
            Menu.update()
            Menu.draw()
        elif GameMode.state == singletons.GameMode.GAME:
            Game.update()
            Game.draw()
        elif GameMode.state == singletons.GameMode.PAUSE:
            pass
        elif GameMode.state == singletons.GameMode.SETTINGS:
            pass
        elif GameMode.state == singletons.GameMode.EXIT:
            pass

        pygame.display.update()
        clock.tick(Display.getFPS)

    pygame.quit()


main()
