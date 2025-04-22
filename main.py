import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get(): # Allows Quiting
            if event.type == pygame.QUIT:
                return
    
        player.update(dt) # Updates player posistion

        pygame.Surface.fill(screen, 0) # Draws Screen, then player.
        player.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000 #Limits Framerate to 60 FPS

if __name__ == "__main__":
    main()