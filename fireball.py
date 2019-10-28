import pygame
from pygame.sprite import Sprite
from mario import Mario


class Fireball(Sprite):
    def __init__(self, mario):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([2, 2])
        self.image.fill(pygame.Color("#000000"))

        self.rect = self.image.get_rect()
        self.rect.centerx = mario.rect.centerx

        self.y = float(self.rect.y)

    def draw_fireball(self):
        self.rect.y += 5
