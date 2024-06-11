import pygame
import os

class Enemy(pygame.sprite.Sprite):
    def __init__(self, settings, screen, x, y):
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.image = pygame.image.load(os.path.join('images', 'enemy.png')).convert_alpha()  # Cargar la imagen
        self.image = pygame.transform.scale(self.image, (50, 50))  # Redimensionar la imagen
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 3  # Cantidad de disparos necesarios para destruir al enemigo

    def draw(self):
        # Verificar si el enemigo está dentro de los límites de la pantalla
        if self.rect.right > 0 and self.rect.left < self.settings.screen_width and \
        self.rect.bottom > 0 and self.rect.top < self.settings.screen_height:
            # Dibujar el enemigo solo si está dentro de los límites de la pantalla
            self.screen.blit(self.image, self.rect)

