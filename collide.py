import pygame

class Collide(pygame.sprite.Sprite):
"""The Collide class is used for tile collisions. It creates invisible blocks
that will be later set to be uncollidable."""

  def __init__(self, x, y, width, height, name='default_collider')
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface((width, height)).convert()
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.state = None
