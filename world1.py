import sys
import pygame
import time

from mario import Mario

m = Mario()


class Camera(object):
    def __init__(self, function, width, height):
        self.function = function
        self.state = pygame.Rect(0, 0, width, height)

    def apply(self, m):
        return m.rect.move(self.state.topleft)

    def update(self, m):
        self.state = self.function(self.state, m.rect)
        # self.state = self.function(self.state, Mario.rect)


def view_camera(camera, m):
    x = -m.center[0] + WIDTH / 2
    camera.topleft += x
    camera.x = max(-(camera.width - WIDTH), min(0, camera.x))
    return camera


WIDTH = 225
HEIGHT = 240
screen = pygame.display.set_mode((WIDTH, HEIGHT))
world1 = pygame.Rect(0, 0, 225, 3392)
map1 = pygame.image.load('assets/maps/World_1-1.png')
clock = pygame.time.Clock()
camera = Camera(view_camera, 225, 3392)
worldOn = True


# Sprite Lists
mario_list = pygame.sprite.Group()  # user
# platform_list = pygame.sprite.Group()  # platforms
all_sprites_list = pygame.sprite.Group()
fireball_list = pygame.sprite.Group()  # fireball

# all_sprites_list.add(Mario)


# Main game loop (to be implemented)
def world1():
    while worldOn:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # Quit
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                # Move Left
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    Mario.moveRight = False
                    Mario.moveLeft = True
                    print('l')

                # Move Right
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    Mario.moveLeft = False
                    Mario.moveRight = True
                    print('r')

                # Run / Shoot Fire
                elif event.key == pygame.K_LSHIFT:
                    # if player.isFire:
                    # Create fireball
                    # fireball = Fireball()
                    # fireball.rect.x = mario.rect.x
                    # fireball.rect.y = mario.rect.y
                    # fireball_list.add(fireball)
                    print('running/shoot fire')

                elif event.key == pygame.K_UP or event.key == pygame.K_SPACE or event.key == pygame.K_w:
                    Mario.jump()
                    print('jump')

                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    print('crouch')

            elif event.type == pygame.KEYUP:
                # Stop moving Left
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    Mario.moveLeft = False

                # Stop moving Right
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    Mario.moveRight = False

                # Stop moving up
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    Mario.moveUp = False

                # Stop crouching
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    Mario.moveDown = False

                elif event.key == pygame.K_UP or event.key == pygame.K_SPACE or event.key == pygame.K_w:
                    Mario.jumping = True

        all_sprites_list.update()

        # draw background
        ...
        camera.update(m)  # camera follows player
        m.update()  # update player

        for e in entities:
            # apply the offset to each entity
            # call this for everything that should scroll,
            # i.e. everything other than HUD
            screen.blit(e.image, camera.apply(e))

        pygame.display.update()
