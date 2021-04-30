import math
import random

class PVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.max = .1
        
    def add(self, v):
        self.y = self.y + v.y
        self.x = self.x + v.x
        
    def sub(self, v):
        self.y = self.y + v.y
        self.x = self.x + v.x
        
    def mult(self, n):
        self.x = self.x * n
        self.y = self.y * n
        
    def div(self, n):
        self.x = self.x / n
        self.y = self.y / n   
        
    def mag(self):
        return math.sqrt(self.x*self.x + self.y*self.y)
        
    def normalize(self):
        m = self.mag()
        if m != 0:
            self.div(m)
            
    def limit(self, max_mag):
        if( self.mag() ) > max_mag:
            self.set_mag(max_mag)
            
    def set_mag(self, mag):
        self.normalize()
        self.mult(mag)
         
    def __add__(self, v):
        new_v = PVector( self.x+v.x, self.y+v.y)
        return new_v   
        
    def __sub__( self,v):
        new_v = PVector( self.x-v.x, self.y-v.y)
        return new_v
        
    def __mul__( self, n):
        new_v = PVector( self.x * n, self.y * n)
        return new_v
        
    def __truediv__( self, n):
        
        new_v = PVector( self.x / n, self.y / n)
        #print (self.x,self.y, new_v.x,new_v.y)
        return new_v
        
    @staticmethod
    def random2D():
        x=random.uniform(-360,360)
        y=random.uniform(-360,360)
        v = PVector(x,y)
        v.normalize()
        return v
         
    @staticmethod
    def div_static(v,n):
        new_v = PVector( v.x/n, v.y/n)
        return new_v 
"""        
    @staticmethod
    def mult(v,n):
        new_v = PVector( v.x*n, v.y*n)
        return new_v 
"""   


