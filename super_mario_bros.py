import sys
import pygame

# import files


pygame.init()
screen = pygame.display.set_mode((256, 240))
pygame.display.set_caption("Super Mario Bros")

# Flags for game loop
gameOn = False
worldCount = 1

# create title screen; initialize everything
title = pygame.Rect(0, 0, 256, 240)
smbTitle = pygame.image.load('assets/Title.png')
screen.blit(smbTitle, title)

def run_game():
    if worldCount == 1:
        world1()
    if worldCount == 2:
        world2()
    if worldCount == 3:
        world3()
    if worldCount == 4:
        world4()

while gameOn == False:
    # set gameOn to "True" when button is pressed
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            gameOn = True
        
while gameOn == True:
    run_game()

pygame.quit()
sys.exit()
