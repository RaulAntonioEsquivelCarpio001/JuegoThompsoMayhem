import pygame
from settings import Settings
from game import Game

def main():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("My Game")

    show_start_screen(screen, settings)

    game = Game(screen, settings)
    game.player.game = game
    while True:
        game.run()

def show_start_screen(screen, settings):
    start_image = pygame.image.load('images/doflamingo.jpg')
    start_image = pygame.transform.scale(start_image, (settings.screen_width, settings.screen_height))

    font = pygame.font.Font(None, 74)
    title_text = font.render("Mata e impresioname", True, (36, 4, 48))
    title_rect = title_text.get_rect(center=(settings.screen_width / 2, settings.screen_height / 4))

    button_rect = pygame.Rect(0, 0, 200, 50)
    button_rect.center = (settings.screen_width / 2, settings.screen_height * 3 / 4)
    font = pygame.font.Font(None, 36)
    button_text = font.render("Iniciar Juego", True, (255, 255, 255))
    button_text_rect = button_text.get_rect(center=button_rect.center)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button_rect.collidepoint(mouse_pos):
                    return

        screen.blit(start_image, (0, 0))
        screen.blit(title_text, title_rect)
        pygame.draw.rect(screen, (0, 0, 255), button_rect)
        screen.blit(button_text, button_text_rect)

        pygame.display.flip()

if __name__ == "__main__":
    main()
