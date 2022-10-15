from cgi import test
from ParticleObject import *
from scene import scene

u_width, u_height = unicorn.get_shape()


velocity = [1,1]
part1 = ParticleObject(1,1,velocity)

def test4():
    #display a particle
    s = scene(0,0)
    s.create_physics_object(part1)
    try:
        while(True):
            s.render()
            time.sleep(0.5)
            part1.updateposition()
            s.clear()
    except KeyboardInterrupt:
        s.clear()

test4()