import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    running = True

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    updatable = [player]
    drawable = [player]

    Player.containers = (updatable, drawable)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for obj in updatable:
            obj.update(dt)
        
        screen.fill('black')

        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == '__main__':
    main()

