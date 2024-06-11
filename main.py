import pygame
from settings import Settings
from game import Game

def main():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("My Game")

    game = Game(screen, settings)
    game.player.game = game  # Pasar la instancia de Game al jugador
    while True:
        game.run()

if __name__ == "__main__":
    main()
