from cgi import test
import sys
sys.path.append('../python-physics-engine')
from ParticleObject import * 
from scene import *

u_width, u_height = unicorn.get_shape()

v1 = [1,0]
part1 = ParticleObject(1,1,v1)

v2 = [-1,0]
part2 = ParticleObject(15,1,v2)

def test5():
    #display 2 particles
    s = scene(0,0)
    s.create_physics_object(part1)
    s.create_physics_object(part2)
    try:
        while(True):
            s.render()
            unicorn.show()
            time.sleep(0.5)
            s.update()
            if s.detect_collision():
                break
            s.clear()
    except KeyboardInterrupt:
        s.clear()

test5()