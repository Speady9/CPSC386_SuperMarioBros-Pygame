import sys
import pygame
import time

from Mario import Mario

WIDTH = 225
HEIGHT = 240
screen = pygame.display.set_mode((WIDTH, HEIGHT))
world1 = pygame.Rect(0, 0, 225, 3392)
map1 = pygame.image.load('assets/maps/World_1-1.png')
clock = pygame.time.Clock()
camera = Camera(view_camera, 225, 3392)

def view_camera(camera, player):
	x = -player.center[0] + WIDTH/2
	camera.topleft += (x - camera.topleft * 0.06)
	camera.x = max(-(camera.width-WIDTH), min(0, camera.x))
	return camera

class Camera(object):
	def __init__(self, function, width, height):
		self.function = function
		self.state = Rect(0, 0, width, height)
	
	def apply(self, player):
		return player.rect.move(self.state.topleft)
		
	def update(self, player):
		self.state = self.function(self.state, player.rect)
		
		
# Main game loop (to be implemented)
while (...):
	# draw background
	...
	camera.update(player) # camera follows player
	player.update() # update player

	for e in entities:
		# apply the offset to each entity
		# call this for everything that should scroll,
		# i.e. everything other than HUD
		screen.blit(e.image, camera.apply(e))
	
	pygame.display.update()