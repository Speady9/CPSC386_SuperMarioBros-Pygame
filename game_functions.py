import sys

import pygame


def check_events():
    """Responds to keypress"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def check_goomba_edges(ai_settings, enemy):
    """sees if enemy hits an edge"""
    if enemy.check_edges():
        change_goomba_direction(ai_settings)


def change_goomba_direction(ai_settings):
    ai_settings.goomba_direction *= -1


def check_koopa_edges(ai_settings, enemy):
    """sees if enemy hits an edge"""
    if enemy.check_edges():
        change_koopa_direction(ai_settings)


def change_koopa_direction(ai_settings):
    ai_settings.koopa_direction *= -1


def update_screen(ai_settings, screen, goomba, koopa):
    """Updates images on screen"""
    # Draw screen
    screen.fill(ai_settings.bg_color)
    # Draw enemies
    goomba.blitme()
    koopa.blitme()
    # Make screen visible
    pygame.display.flip()


def update_goomba(ai_settings, goomba):
    """Updates position of goomba"""
    check_goomba_edges(ai_settings, goomba)
    goomba.update()


def check_collision(ai_settings, enemy1, enemy2):
    if enemy1.colliderect(enemy2):
        change_goomba_direction(ai_settings)
        change_koopa_direction(ai_settings)


def update_koopa(ai_settings, koopa):
    """Updates position of koopa"""
    check_koopa_edges(ai_settings, koopa)
    koopa.update()
