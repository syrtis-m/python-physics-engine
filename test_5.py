from cgi import test
from ParticleObject import *
from scene import *

u_width, u_height = unicorn.get_shape()

def clear():
    for i in range(0,u_width):
        for j in range (0,u_height):
            unicorn.set_pixel(i,j,0,0,0)

v1 = [1,0]
part1 = ParticleObject(1,1,v1)

v2 = [-1,0]
part2 = ParticleObject(15,1,v2)

def test4():
    #display 2 particles
    try:
        while(True):
            part1.render()
            part2.render()
            unicorn.show()
            time.sleep(0.5)
            part1.updateposition()
            part2.updateposition()
            clear()
    except KeyboardInterrupt:
        clear()

test4()