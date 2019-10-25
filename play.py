import sys

import pygame

from settings import Settings
from goomba import Goomba
from koopa import  Koopa
import game_functions as gf


def run_game():
    # Initialize game and create the screen
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Super Mario Bros")

    goomba = Goomba(ai_settings, screen)
    koopa = Koopa(ai_settings, screen)
    # Start the main loop
    while True:
        gf.check_events()
        gf.update_goomba(ai_settings, goomba)
        gf.update_koopa(ai_settings, koopa)
        gf.update_screen(ai_settings, screen, goomba, koopa)


run_game()
