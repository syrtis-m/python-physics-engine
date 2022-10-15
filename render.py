from AbstractObject import *


def test():
    unicorn.set_pixel(1, 1, 235, 64, 52)
    unicorn.show()

#pass a list of objects derived from AbstractObject and then call render on each of them
def render_objects(list):
    for object in list:
        object.render()
    unicorn.show()