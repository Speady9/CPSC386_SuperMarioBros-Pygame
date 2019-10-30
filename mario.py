import pygame
from pygame.sprite import Sprite
vec2 = pygame.math.Vector2


class Mario(Sprite):

    def __init__(self, x, y, width, height):
        # call parent class
        pygame.sprite.Sprite.__init__(self)

        # initialize
        self.width = width
        self.height = height
        self.onGround = True
        self.crouching = False
        self.jumping = False

        # variables for jumping
        self.velX, self.velY = 0, 0
        self.vel = vec2(0, 0)
        self.accX, self.accY = 0, 0
        self.acc = vec2(0, 0)
        self.fri = float(-0.30)

        #  create rect
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(pygame.Color("#008080"))
        self.rect = self.image.get_rect()

        #  rect placement
        self.pos = vec2(x, y)
        # self.rect.centerx = x
        # self.rect.bottom = y

    # load Mario
    # self.image = pygame.image.load('images/INSERT')
    # self.image = pygame.transform.scale(self.image, (10, 20))

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

    def becomeSmall(self):
        isSmall = True
        isBig = False
        isFire = False
        isStar = False
        pygame.transform.scale(self.rect, (16, 16))

    def becomeBig(self):
        isSmall = False
        isBig = True
        isFire = False
        isStar = False

        # Should transform mario into a bigger rect.
        pygame.transform.scale(self.rect, (16, 32))

    # Add allowing to shoot fireballs
    def becomeFire(self):
        isSmall = False
        isBig = False
        isFire = True
        isStar = False

    # Add no damage from collisions (should set a timer for it to run out)
    def becomeStar(self):
        isSmall = False
        isBig = False
        isFire = False
        isStar = True

    def jump_cut(self):
        if self.jumping:
            if self.vel.y < float(.00025):
                self.vel.y = float(.00025)

    def jump(self):
        if not self.jumping:
            self.vel.y = float(-.25)
            self.jumping = True

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

    # reset the player to the mid of the screen change to when colliding with enemy sprites
    def die(self):
        self.pos = (900/2, 600/2)

    def win(self):
        pass

    def update(self):
        r = self.rect

        # movement speed
        self.acc = vec2(0, float(.00025))  # Y affects gravity

        if self.moveDown and r.bottom < 600:
            r.centery += self.velX

        if self.moveUp and r.top > 0:
            r.centery -= self.velX

        if self.moveLeft and r.left:
            self.acc.x = float(-0.08)
            r.centerx -= self.velX

        if self.moveRight and r.right:
            self.acc.x = float(0.08)
            r.centerx += self.velX

        # apply friction
        self.acc.x += self.vel.x * self.fri
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + float(0.1) * self.acc

        # wrap around screen
        if self.pos.x > 890:
            self.pos.x = 10
        if self.pos.x < 10:
            self.pos.x = 890

        self.rect.midbottom = self.pos


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(pygame.Color("#800080"))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
