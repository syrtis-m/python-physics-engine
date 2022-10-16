from AbstractObject import *

class BallObject(AbstractObject):
    def __init__(self, x, y, velocity, color) -> None:
        self.velocity = velocity #velocity is (x,y) tuple
        self.x = x
        self.y = y
        self.r = color[0]
        self.g = color[1]
        self.b = color[2]
    
    def render(self):
        unicorn.set_pixel(int(self.x),int(self.y),self.r,self.g,self.b)
        #unicorn.set_pixel(self.x+1, self.y, self.r,self.g,self.b)
        #unicorn.set_pixel(self.x,self.y+1,self.r,self.g,self.b)
        #unicorn.set_pixel(self.x-1,self.y,self.r,self.g,self.b)
        #unicorn.set_pixel(self.x,self.y-1,self.r,self.g,self.b)
        # TODO re-add these once bounces get working

        

    def updatePosition(self): #velocity and gravity need to be considered
        self.x += self.velocity[0]
        self.y += self.velocity[1]

    def isOutOfBounds(self):
        return super().isOutOfBounds()

    def addForce(self, force: tuple):
        return super().addForce(force)