import pygame
from pygame.sprite import Sprite


class Redkoopa(Sprite):
    """Class that represents one Red Koopa"""

    def __init__(self, ai_settings, screen):
        super(Redkoopa, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the Red Koopa image
        self.image = pygame.image.load('assets/sprites/enemies/red_koopa_left1.png')
        self.rect = self.image.get_rect()

        # Setting position of Red Koopa
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the Red Koopa's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the Red Koopa at it's current location"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Returns True if Red Koopa hits edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move Red Koopa left of right"""
        self.x += (self.ai_settings.enemy_speed_factor * self.ai_settings.goomba_direction)
        self.rect.x = self.x