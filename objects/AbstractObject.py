import sys
sys.path.append('../python-physics-engine')

from abc import ABC, abstractmethod
import numpy as np
import math
import time
from timeit import default_timer as timer


try:
    import unicornhathd as unicorn
    print("unicorn hat hd detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd as unicorn


#all objects inherit from this
class AbstractObject(ABC):

    def __init__(self, x, y, velocity, color, object_specific_setup) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.v = velocity #velocity is (x,y) tuple
        self.r = color[0]
        self.g = color[1]
        self.b = color[2]

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def updatePosition(self):
        pass

    @abstractmethod
    def isOutOfBounds(self):
        if ((self.x > 15) or (self.x < 0)):
            return True
        if ((self.y >15) or (self.y < 0)):
            return True
        return False

    @abstractmethod
    def addForce(self, force):
        self.velocity = (self.velocity[0] + force[0], self.velocity[1] + force[1])
