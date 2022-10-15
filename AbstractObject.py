from abc import ABC, abstractmethod
import numpy as np
import time
from timeit import default_timer as timer



try:
    import unicornhathd as unicorn
    print("unicorn hat hd detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd as unicorn


#all objects inherit from this
class AbstractObject(ABC):

    def __init__(self, x, y, velocity, object_specific_setup) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.v = velocity

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def updateposition(self):
        pass