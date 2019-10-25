import pygame
import sys

class Mario:

    def __init__(self, settings):
        self.settings = settings

    # load Mario
    # self.image = pygame.image.load('images/INSERT')
    # self.image = pygame.transform.scale(self.image, (10, 20))
    # self.rect = self.image.get_rect()
    # self.screen_rect = screen.get_rect()

    # r, sr = self.rect, self.screen_rect
    #
    # # Mario at the bottom
    # r.centerx = sr.centerx
    # r.bottom = sr.bottom

    # Set up keyboard variables.
    moveLeft = False
    moveRight = False
    moveUp = False
    moveDown = False

    # Player States
    isSmall = True
    isBig = False
    isFire = False
    isStar = False

    # Environment
    isInWater = False

    # player move
    MOVESPEED = 5

    def player_move(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # Quit
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                # Move Left
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.moveRight = False
                    self.moveLeft = True
                    print('l')

                # Move Right
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.moveLeft = False
                    self.moveRight = True
                    print('r')

                # Run / Shoot Fire
                elif event.key == pygame.KMOD_LSHIFT:
                    self.MOVESPEED *= 2
                    if self.isFire == True:
                        self.shootfireball()

                # Jump (Add short vs small jump)
                elif event.key == pygame.K_SPACE or pygame.K_w:
                    print('jump')

                # Crouch
                elif event.key == pygame.K_DOWN or pygame.K_s:
                    print('crouch')

            if event.type == pygame.KEYUP:
                # Quit
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                # Stop moving Left
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.moveLeft = False

                # Stop moving Right
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.moveRight = False

                # Stop moving up
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.moveUp = False

                # Stop crouching
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.moveDown = False

    def becomeSmall(self):
        isSmall = True
        isBig = False
        isFire = False
        isStar = False

    def becomeBig(self):
        isSmall = False
        isBig = True
        isFire = False
        isStar = False

    def becomeFire(self):
        isSmall = False
        isBig = False
        isFire = True
        isStar = False

    def becomeStar(self):
        isSmall = False
        isBig = False
        isFire = False
        isStar = True

    def shootfireball(self):
        pass

    def player_collision(self):
        # Add collision with collectibles + insert lines for collision with enemies/blocks
        if self.isSmall:
            self.die()
        if self.isBig():
            self.becomeSmall()
        if self.isFire:
            self.becomeBig()

    def die(self):
        pass

    def win(self):
        pass

    def update(self):
        r, sr = self.rect, self.screen_rect

        # if self.moving_right and r.right < sr.right:
        #     r.centerx += self.MOVESPEED
        # if self.moving_left and r.left > 0:
        #     r.centerx -= self.MOVESPEED

        if self.moveDown and r.bottom < settings.WINDOWHEIGHT:
            r.centery += self.MOVESPEED

        if self.moveUp and r.top > 0:
            r.centery -= self.MOVESPEED

        if self.moveLeft and r.left > 0:
            r.centerx -= self.MOVESPEED

        if self.moveRight and r.right < settings.WINDOWWIDTH:
            r.centerx += self.MOVESPEED

