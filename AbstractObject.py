from abc import ABC, abstractmethod
import numpy as np
import time


try:
    import unicornhathd as unicorn
    print("unicorn hat hd detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd as unicorn

#all objects inherit from this
class AbstractObject(ABC):

    def __init__(self, object_specific_setup) -> None:
        super().__init__()

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def updateposition(self):
        pass