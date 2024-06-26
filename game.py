import pygame
from player import Player
from enemy import Enemy

class Game:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.player = Player(settings, screen)
        self.player.game = self  # Pasar la instancia del juego al jugador
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_over = False  # Flag para game over

        # Inicializar enemigos y rondas
        self.enemies = pygame.sprite.Group()
        self.current_round = 1
        self.round_enemies = 3  # Enemigos iniciales por ronda
        self.enemies_killed = 0

        # Lista para rastrear balas a eliminar
        self.bullets_to_remove = []

        # Crear enemigos iniciales
        self._create_enemies()

    def _create_enemies(self):
        self.enemies.empty()  # Vaciar el grupo de enemigos
        for _ in range(self.round_enemies):
            x, y = self._generate_random_position()
            enemy = Enemy(self.settings, self.screen, x, y)
            self.enemies.add(enemy)

    def _generate_random_position(self):
        import random
        x = random.randint(0, self.settings.screen_width - self.settings.enemy_size[0])
        y = random.randint(0, self.settings.screen_height - self.settings.enemy_size[1])
        return x, y

    def run(self):
        while self.running:
            self._check_events()
            if self.game_over:
                self._show_game_over()
                pygame.time.wait(5000)  # Esperar 5 segundos
                pygame.quit()
                quit()  # Cerrar el juego
            else:
                self.player.update()
                self.enemies.update()  # Actualizar posiciones de los enemigos
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

        # Comprobar colisiones entre balas y enemigos
        collisions = pygame.sprite.groupcollide(self.player.bullets, self.enemies, False, False)
        for bullet, hit_enemies in collisions.items():
            for enemy in hit_enemies:
                enemy.take_damage()
                bullet.hits += 1  # Incrementar los golpes para la bala

                if bullet.hits >= 2:
                    self.bullets_to_remove.append(bullet)

        # Eliminar balas que han golpeado suficiente veces
        for bullet in self.bullets_to_remove:
            self.player.bullets.remove(bullet)

        # Dibujar enemigos que aún están vivos
        for enemy in self.enemies:
            enemy.draw()

        self._draw_ui()
        self._draw_buttons()
        pygame.display.flip()

        # Comprobar si todos los enemigos han sido eliminados
        if not self.enemies:
            self._next_round()

    def _next_round(self):
        self.current_round += 1
        if self.current_round % 3 == 1:
            self.round_enemies += 1
        self.player.reload_bullets()  # Recargar balas
        self._create_enemies()

    def _draw_ui(self):
        font = pygame.font.Font(None, 36)
        bullets_text = font.render(f'Bullets: {len(self.player.bullets)}/{self.settings.bullets_allowed}', True, (255, 255, 255))
        bullets_text_rect = bullets_text.get_rect()
        bullets_text_rect.topright = (self.settings.screen_width - 20, 20)
        self.screen.blit(bullets_text, bullets_text_rect)

        round_text = font.render(f'Round: {self.current_round}', True, (255, 255, 255))
        round_text_rect = round_text.get_rect()
        round_text_rect.topright = (self.settings.screen_width - 20, 60)
        self.screen.blit(round_text, round_text_rect)

    def _check_mouse_click(self, event):
        mouse_pos = pygame.mouse.get_pos()
        if event.button == 1:  # Botón izquierdo del ratón
            exit_button_rect = pygame.Rect(20, 20, 100, 50)
            if exit_button_rect.collidepoint(mouse_pos):
                pygame.quit()
                quit()

    def _draw_buttons(self):
        # Botón de salida
        exit_button_rect = pygame.Rect(20, 20, 100, 50)
        pygame.draw.rect(self.screen, (0, 0, 255), exit_button_rect)
        font = pygame.font.Font(None, 36)
        text = font.render("Exit", True, (255, 255, 255))
        text_rect = text.get_rect(center=exit_button_rect.center)
        self.screen.blit(text, text_rect)

    def _show_game_over(self):
        font = pygame.font.Font(None, 74)
        game_over_text = font.render("GAME OVER", True, (255, 0, 0))
        game_over_rect = game_over_text.get_rect(center=(self.settings.screen_width / 2, self.settings.screen_height / 2))
        self.screen.blit(game_over_text, game_over_rect)
        pygame.display.flip()
