import sys
sys.path.append('../python-physics-engine')
sys.path.append('../python-physics-engine/objects')
from objects.ParticleObject import *
from scene import *

u_width, u_height = unicorn.get_shape()


velocity = [1,1]
part1 = ParticleObject(1,1,velocity,(255,255,255))

def test4():
    #display a particle
    s = scene(forcesZeroG)
    s.create_physics_object(part1)
    try:
        while(True):
            s.render()
            time.sleep(0.5)
            part1.updatePosition()
            s.clear()
    except KeyboardInterrupt:
        s.clear()

test4()