import pygame
from pygame.sprite import Sprite


class Greencheep(Sprite):
    """Class that represents one Green Cheep"""

    def __init__(self, ai_settings, screen):
        super(Greencheep, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the Green Cheap image
        self.image = pygame.image.load('assets/sprites/enemies/g_cheep_left1.png')
        self.rect = self.image.get_rect()

        # Setting position of Green Cheep
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the Green Cheep's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the Green Cheap at it's current location"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Returns True if Green Cheep hits edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move Green Cheep left of right"""
        self.x += (self.ai_settings.enemy_speed_factor * self.ai_settings.goomba_direction)
        self.rect.x = self.x