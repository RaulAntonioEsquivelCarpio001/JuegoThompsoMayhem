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
        self.hits = 0  # New attribute to track how many times the enemy has been hit

    def update(self):
        pass  # Currently empty, add logic as per your game requirements

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def take_damage(self):
        self.hits += 1
        if self.hits >= 1:
            self.kill()  # Remove the enemy from all sprite groups
