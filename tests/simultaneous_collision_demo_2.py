import sys
from timeit import default_timer as timer

sys.path.append('../python-physics-engine')
sys.path.append('../python-physics-engine/objects')
from objects.ParticleObject import *
from scene import *
u_width, u_height = unicorn.get_shape()

animation_speed = 0.1

def demo2(waittime):

    part1 = ParticleObject(14,1,[-1,2],(255,0,255))
    part2 = ParticleObject(14,14,[-1,-2],(0,255,255))
    part3 = ParticleObject(1,1,[1,2],(255,255,0))
    part4 = ParticleObject(1,14,[1,-2],(0,0,255))

    s = scene(forcesZeroG)
    s.create_physics_object(part1)
    s.create_physics_object(part2)
    s.create_physics_object(part3)
    s.create_physics_object(part4)

    try:
        start = timer()
        end = timer()
        while ((end-start) < float(waittime)):
            s.render()
            unicorn.show()
            time.sleep(animation_speed)
            s.update()
            s.clear()
            end = timer()
    except KeyboardInterrupt:
        s.clear()

#demo2()