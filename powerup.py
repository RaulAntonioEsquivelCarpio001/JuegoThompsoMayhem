import pygame
import random

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, settings, screen):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('images/powerup.jpg')
        self.image = pygame.transform.scale(self.image, (30, 30))  # Tamaño del power-up
        self.rect = self.image.get_rect()

        self.rect.x = random.randint(0, self.settings.screen_width - self.rect.width)
        self.rect.y = random.randint(0, self.settings.screen_height - self.rect.height)

    def draw(self):
        self.screen.blit(self.image, self.rect)
