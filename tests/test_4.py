import sys
sys.path.append('../python-physics-engine')
sys.path.append('../python-physics-engine/objects')
from objects.ParticleObject import *
from scene import *

u_width, u_height = unicorn.get_shape()


velocity = [1,1]
part1 = ParticleObject(1,1,velocity,(255,255,255))

def test4(waittime):
    #display a particle
    s = scene(forcesZeroG)
    s.create_physics_object(part1)
    start = timer()
    end = timer()
    try:
        while((end-start) < float(waittime)):
            s.render()
            time.sleep(0.5)
            part1.updatePosition()
            s.clear()
            end = timer()
    except KeyboardInterrupt:
        s.clear()

#test4(5)