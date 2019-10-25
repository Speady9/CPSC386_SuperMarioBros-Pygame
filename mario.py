import pygame


class Mario(object):

    def __init__(self, x, y):
        self.xcor = x
        self.ycor = y
    # load Mario
    # self.image = pygame.image.load('images/INSERT')
    # self.image = pygame.transform.scale(self.image, (10, 20))
    rect = pygame.Rect(900/2, 600/2, 10, 20)
    # screen_rect = screen.get_rect()

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
    moveSpeed = 2

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

    def shootFire(self):  # make a separate class for the obj
        pass

    def player_collision(self):
        # Add collision with collectibles + insert lines for collision with enemies/blocks
        if self.isSmall:
            self.die()
        if self.isBig:
            self.becomeSmall()
        if self.isFire:
            self.becomeBig()

    def die(self):
        pass

    def win(self):
        pass

    def update(self):
        r = self.rect

        if self.moveDown and r.bottom < 600:
            r.centery += self.moveSpeed

        if self.moveUp and r.top > 0:
            r.centery -= self.moveSpeed

        if self.moveLeft and r.left > 0:
            r.centerx -= self.moveSpeed

        if self.moveRight and r.right < 900:
            r.centerx += self.moveSpeed
