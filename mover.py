from pvector import *
import pygame


class Mover:
    def __init__(self,x,y):
        self.speed = PVector(0,0)
        self.location = PVector(x,y)
        self.accel = PVector(0, 0)
        self.radius = 10
        self.color = (0,0,255)
        self.mass = 10
        self.x_max = 10
        self.y_max = 10
        
    def update(self):
        self.speed.x = self.speed.x + self.accel.x
        self.speed.y = self.speed.y + self.accel.y  
        
        self.speed.limit(self.speed.max)
        
        self.location.x = self.location.x + self.speed.x
        self.location.y = self.location.y + self.speed.y
        self.constrain(self.x_max,self.y_max)
        self.accel.mult(0)
        
    def apply_force(self,force):
        a = force/self.mass
        #f = PVector.div_static(force, self.mass)
        self.accel.add(a)
        
    def apply_acceleration(self, a):
        self.accel.add(a)
        
    def draw(self, surface):
        pygame.draw.circle( surface, self.color, (int(self.location.x),int(self.location.y)), self.radius)
        
    def constrain(self, x_max, y_max):
        if self.location.x >x_max + self.radius:
            self.location.x = 0 - self.radius
        elif self.location.x < 0 - self.radius:
            self.location.x = x_max + self.radius
                
        #if self.location.y > y_max + self.radius:
            #self.location.y = 0 - self.radius
        if self.location.y < 0 - self.radius:
            self.location.y = y_max + self.radius
            
        if self.location.y > y_max - self.radius:
            self.location.y = y_max - self.radius
