from AbstractObject import *

class ParticleObject(AbstractObject):
    def __init__(self, x, y, velocity) -> None:
        self.velocity = velocity
        self.x = x
        self.y = y
    
    def render(self):
        unicorn.set_pixel(self.x,self.y,255,255,255)

    def updateposition(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]
