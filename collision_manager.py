# collison manager takes n objects (physics or static) that scene has decided have collided and decides what to do with the collision
import sys
sys.path.append('/objects')
from objects.ParticleObject import ParticleObject

class CollisionManager():
    def __init__(self) -> None:
        pass

    def phys_phys_handler(self, obj1, obj2):
        v3 = (obj1.velocity[0] + obj2.velocity[0]),(obj1.velocity[1] + obj2.velocity[1])
        x3 = int((obj1.x + obj2.x) / 2) 
        y3 = int((obj1.y + obj2.y)/2)
        obj3 = ParticleObject(x3,y3,v3,(255,0,0))
        return obj3
    