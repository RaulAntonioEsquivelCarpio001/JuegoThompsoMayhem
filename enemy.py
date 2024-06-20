import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, settings, screen, x, y):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('images/enemy.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hits = 0  # Track how many times the enemy has been hit

        # Initialize enemy speed and direction
        self.speed_x = self.settings.enemy_speed_x
        self.speed_y = self.settings.enemy_speed_y

    def update(self):
        # Move the enemy
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Change direction when hitting the screen edges
        if self.rect.right >= self.settings.screen_width or self.rect.left <= 0:
            self.speed_x *= -1
        if self.rect.bottom >= self.settings.screen_height or self.rect.top <= 0:
            self.speed_y *= -1

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def take_damage(self):
        self.hits += 1
        if self.hits >= 1:
            self.kill()  # Remove the enemy from all sprite groups
