import math
import pygame
from pvector import *

	
# Simple pygame program

def distance(x1,y1,x2,y2):
    x_terms = (x2-x1)**2
    
    y_terms = (y2-y1)**2
    
    return math.sqrt(x_terms + y_terms)
    
def Fg():
    G = 1
    dist = distance(ball_location.x,ball_location.y, 500,500)
    return (G * ball_mass * center_mass)/(dist*dist)
    
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([1000, 1000])

# Run until the user asks to quit
running = True

ball_speed = PVector(1,-1)
ball_accel = PVector(1,1)
ball_location = PVector(20,20)
ball_mass = 100
center_mass = 200000000000

clock = pygame.time.Clock()

#f = open("gravity.csv", "w")
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 0), (500, 500), 20)
    
    pygame.draw.circle( screen, (0,0,255), (ball_location.x,ball_location.y), 10)
    
    ball_speed.add(ball_accel)
    ball_location.add(ball_speed)

    # Flip the display
    pygame.display.flip()
    #print(ball_x_vel)
    print( str(distance(ball_location.x, ball_location.y, 500,500))+","+str( Fg())+"\n" )
    
    clock.tick(24)

# Done! Time to quit.
pygame.quit()
