# collison manager takes n objects (physics or static) that scene has decided have collided and decides what to do with the collision
import sys
import numpy as np
from objects.BallObject import BallObject
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

    def phys_stat_handler(self, phys, stat, gravity, friction, COR):
        #find normal vector for stat. we have slope in stat[2]
        statNormVec = np.array((-stat[2],1))
        velocity = np.array(phys.velocity)
        #find u and v for phys from phys.velocity
        u = ((np.dot(velocity, statNormVec)) / (np.dot(statNormVec,statNormVec))) * statNormVec
        w = velocity - u

        newVelocity = (friction*w) - (COR*u)
        newVelocity = (newVelocity[0], newVelocity[1])
        newObj = BallObject(phys.x,phys.y,newVelocity,(phys.r,phys.g,phys.b))
        return newObj