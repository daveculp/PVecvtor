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
movers = []
for i in range(2000):
    mover = Mover( random.randint(0,SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT) )
    mover.speed.max = 5
    mover.x_max = SCREEN_WIDTH
    mover.y_max = SCREEN_HEIGHT
    mover.radius = random.randint(1,20)
    mover.mass = mover.radius**2
    mover.color = ( random.randint(0,255), random.randint(0,255), random.randint(0,255))
    movers.append(mover)
ball = Mover(500,500)
ball.speed.max = 5
ball.radius = 50

mouse_x, mouse_y = pygame.mouse.get_pos()
mouse = PVector(mouse_x, mouse_y)
wind = PVector(-200,6)


# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))
    
    mouse.x, mouse.y = pygame.mouse.get_pos()
    mouse_dir = PVector.sub( mouse,ball.location)
    mouse_dir = mouse - ball.location
    mouse_dir.normalize()
    mouse_dir.mult(.1)
    
    ball.accel = mouse_dir
    
    for i in range(len(movers)):
        
        acceleration = PVector.random2D()
        #print(acceleration.x, acceleration.y)
        movers[i].accel = acceleration
        #print(acceleration.y, ball.accel.y)
        movers[i].apply_force(wind)
        #print(movers[i].mass)
        movers[i].update()
        ball.constrain(SCREEN_WIDTH, SCREEN_HEIGHT)
        movers[i].draw(screen)
    
    # Flip the display
    screen.blit(update_fps(), (10,0))
    update_fps()
    pygame.display.flip()

    clock.tick(60)

# Done! Time to quit.
pygame.quit()
