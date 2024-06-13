import pygame
from player import Player
from enemy import Enemy

class Game:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.player = Player(settings, screen)
        self.player.game = self  # Pass the game instance to the player
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_over = False  # Flag for game over

        # Initialize enemies
        self.enemies = pygame.sprite.Group()
        self._create_enemies()

        # List to track bullets to remove
        self.bullets_to_remove = []

    def _create_enemies(self):
        positions = [(100, 100), (200, 200), (300, 300), (400, 400)]
        for pos in positions:
            enemy = Enemy(self.settings, self.screen, *pos)
            self.enemies.add(enemy)

    def run(self):
        while self.running:
            self._check_events()
            if self.game_over:
                self._show_game_over()
                pygame.time.wait(5000)  # Wait for 5 seconds
                pygame.quit()
                quit()  # Close the game
            else:
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
        self.player.update()
        self.player.blitme()

        # Check collisions between bullets and enemies
        collisions = pygame.sprite.groupcollide(self.player.bullets, self.enemies, False, False)
        for bullet, hit_enemies in collisions.items():
            for enemy in hit_enemies:
                enemy.take_damage()
                bullet.hits += 1  # Increment hits for the bullet

                if bullet.hits >= 2:
                    self.bullets_to_remove.append(bullet)

        # Remove bullets that have hit enough times
        for bullet in self.bullets_to_remove:
            self.player.bullets.remove(bullet)

        # Draw enemies that are still alive
        for enemy in self.enemies:
            enemy.draw()

        self._draw_ui()
        self._draw_buttons()
        pygame.display.flip()

    def _draw_ui(self):
        font = pygame.font.Font(None, 36)
        text = font.render(f'Balas: {len(self.player.bullets)}/{self.settings.bullets_allowed}', True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.topright = (self.settings.screen_width - 20, 20)
        self.screen.blit(text, text_rect)

    def _check_mouse_click(self, event):
        mouse_pos = pygame.mouse.get_pos()
        if event.button == 1:  # Left mouse button
            exit_button_rect = pygame.Rect(20, 20, 100, 50)
            if exit_button_rect.collidepoint(mouse_pos):
                pygame.quit()
                quit()

    def _draw_buttons(self):
        # Exit button
        exit_button_rect = pygame.Rect(20, 20, 100, 50)
        pygame.draw.rect(self.screen, (0, 0, 255), exit_button_rect)
        font = pygame.font.Font(None, 36)
        text = font.render("Salir", True, (255, 255, 255))
        text_rect = text.get_rect(center=exit_button_rect.center)
        self.screen.blit(text, text_rect)

    def _show_game_over(self):
        font = pygame.font.Font(None, 74)
        game_over_text = font.render("GAME OVER", True, (255, 0, 0))
        game_over_rect = game_over_text.get_rect(center=(self.settings.screen_width / 2, self.settings.screen_height / 2))
        self.screen.blit(game_over_text, game_over_rect)
        pygame.display.flip()
