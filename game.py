import pygame
from player import Player

class Game:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.player = Player(settings, screen)
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            self._check_events()
            self.player.update()
            self._update_screen()
            self.clock.tick(self.settings.fps)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_mouse_click(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = True
        elif event.key == pygame.K_UP:
            self.player.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.player.moving_down = True
        elif event.key == pygame.K_SPACE:
            self.player.shoot()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = False
        elif event.key == pygame.K_UP:
            self.player.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.player.moving_down = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.player.blitme()
        self._draw_ui()
        self._draw_buttons()  # Redibujar botones
        pygame.display.flip()

    def _draw_ui(self):
        font = pygame.font.Font(None, 36)
        text = font.render(f'Balas: {len(self.player.bullets)}/{self.settings.bullets_allowed}', True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.topright = (self.settings.screen_width - 20, 20)
        self.screen.blit(text, text_rect)

    def _check_mouse_click(self, event):
        mouse_pos = pygame.mouse.get_pos()
        if event.button == 1:  # Botón izquierdo del ratón
            # Botón de salida
            exit_button_rect = pygame.Rect(20, 20, 100, 50)
            if exit_button_rect.collidepoint(mouse_pos):
                pygame.quit()
                quit()

    def _draw_buttons(self):
        # Botón de salida
        exit_button_rect = pygame.Rect(20, 20, 100, 50)
        pygame.draw.rect(self.screen, (0, 0, 255), exit_button_rect)
        font = pygame.font.Font(None, 36)
        text = font.render("Salir", True, (255, 255, 255))
        text_rect = text.get_rect(center=exit_button_rect.center)
        self.screen.blit(text, text_rect)
