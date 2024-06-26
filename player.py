import pygame
from bullet import Bullet

class Player:
    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen
        self.image = pygame.image.load('images/player.png')
        self.image = pygame.transform.scale(self.image, self.settings.player_size)
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.center = self.screen_rect.center

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.direction = 'up'

        self.bullets = pygame.sprite.Group()

    def update(self):
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.rect.x += self.settings.player_speed
                self.direction = 'right'
            if self.moving_left and self.rect.left > 0:
                self.rect.x -= self.settings.player_speed
                self.direction = 'left'
            if self.moving_up and self.rect.top > 0:
                self.rect.y -= self.settings.player_speed
                self.direction = 'up'
            if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
                self.rect.y += self.settings.player_speed
                self.direction = 'down'

            self.bullets.update()

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

    def shoot(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self.settings, self.screen, self)
            self.bullets.add(new_bullet)
        elif len(self.bullets) >= self.settings.bullets_allowed:
            self.game.game_over = True  # Set the game over flag
    
    def reload_bullets(self):
        self.bullets = pygame.sprite.Group()