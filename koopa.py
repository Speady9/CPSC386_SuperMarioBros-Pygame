import pygame
from pygame.sprite import Sprite


class Koopa(Sprite):
    """Class that represents one Green Koopa"""

    def __init__(self, ai_settings, screen):
        super(Koopa, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the Green Koopa image
        self.image = pygame.image.load('assets/sprites/enemies/koopa_left1.png')
        self.rect = self.image.get_rect()

        # Setting position of Green Koopa
        self.rect.x = 500
        self.rect.y = 10
        # Store the Green Koopa's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the Green Koopa at it's current location"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Returns True if Green Koopa hits edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move Green Koopa left of right"""
        self.x += (self.ai_settings.enemy_speed_factor * self.ai_settings.koopa_direction)
        self.rect.x = self.x
