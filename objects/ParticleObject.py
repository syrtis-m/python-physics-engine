from AbstractObject import *



class ParticleObject(AbstractObject):
    def __init__(self, x, y, velocity, color) -> None:
        self.velocity = velocity
        self.x = x
        self.y = y
        self.r = color[0]
        self.g = color[1]
        self.b = color[2]
    
    def render(self):
        unicorn.set_pixel(self.x,self.y,self.r,self.g,self.b)

    def updatePosition(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]
    
    def isOutOfBounds(self):
        return super().isOutOfBounds()
    
    def addForce(self, force: tuple):
        return super().addForce(force)