import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, settings, screen, player):
        super().__init__()
        self.screen = screen
        self.settings = settings

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.centerx = player.rect.centerx
        self.rect.top = player.rect.top

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        self.color = self.settings.bullet_color
        self.speed = self.settings.bullet_speed

        self.direction = player.direction

    def update(self):
        if self.direction == 'right':
            self.x += self.speed
        elif self.direction == 'left':
            self.x -= self.speed
        elif self.direction == 'up':
            self.y -= self.speed
        elif self.direction == 'down':
            self.y += self.speed

        self.rect.x = self.x
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
