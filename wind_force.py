import math
import pygame
from pvector import *
from mover import *

def update_fps():
	fps = str(int(clock.get_fps()))
	fps_text = font.render(fps, 1, pygame.Color("coral"))
	return fps_text
				
# Init pygame and set up the drawing window
pygame.init()
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 18)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])


#setup the ball and mouse

ball_1 = Mover(460,538)
ball_1.speed.max = 10
ball_1.radius = ball_1.mass = 2
ball_1.color = (0,0,255)
ball_1.x_max = SCREEN_WIDTH
ball_1.y_max = SCREEN_HEIGHT

ball_2 = Mover(500,500)
ball_2.speed.max = 10
ball_2.radius = ball_2.mass = 40
ball_2.color = (255,0,255)
ball_2.x_max = SCREEN_WIDTH
ball_2.y_max = SCREEN_HEIGHT

wind = PVector(-10,0)
gravity = PVector (0, 9.8)
friction = PVector( 10,0)


# Run until the user asks to quit
running = True
while running:

	# Did the user click the window close button?
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# Fill the background with white
	screen.fill((255, 255, 255))

	ball_1.apply_force(wind)
	ball_2.apply_force(wind)
	
	ball_1.apply_force(friction)
	ball_2.apply_force(friction)
	
	ball_1.apply_acceleration(gravity)
	ball_2.apply_acceleration(gravity)
	
	ball_1.update()
	ball_2.update()
	
	ball_1.draw(screen)
	ball_2.draw(screen)
	
	# Flip the display
	screen.blit(update_fps(), (10,0))
	update_fps()
	pygame.display.flip()

	clock.tick(60)

# Done! Time to quit.
pygame.quit()
