from AbstractObject import *


class StaticObject(AbstractObject):
    def __init__(self, x, y, velocity, object_specific_setup) -> None:
        self.x = x
        self.y = y
        self.velocity = [],0