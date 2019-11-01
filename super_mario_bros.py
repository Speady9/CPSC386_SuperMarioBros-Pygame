import sys
import pygame

# import files
from world1 import world1

pygame.init()
smbTitle = pygame.image.load('assets/title.png')
screen = pygame.display.set_mode(smbTitle.get_rect().size, 0, 32)
pygame.display.set_caption("Super Mario Bros")

# Flags for game loop
gameOn = False
worldCount = 1

# create title screen; initialize everything
title = smbTitle.get_rect()
screen.blit(smbTitle, title)


def run_game():
    if worldCount == 1:
        world1()
    # if worldCount == 2:
        # world2()
    # if worldCount == 3:
        # world3()
    # if worldCount == 4:
        # world4()


while gameOn == False:
    screen.blit(smbTitle, title)
    # set gameOn to "True" when button is pressed
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            gameOn = True


while gameOn == True:
    run_game()

pygame.quit()
sys.exit()
