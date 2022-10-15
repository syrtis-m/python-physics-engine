from cgi import test
from ParticleObject import *
from scene import *

u_width, u_height = unicorn.get_shape()

v1 = [2,0]
part1 = ParticleObject(1,1,v1)

v2 = [-1,0]
part2 = ParticleObject(15,1,v2)

s = scene(0,0)
s.create_physics_object(part1)
s.create_physics_object(part2)

def test6():
    #display 2 particles
    try:
        while(True):
            s.render()
            unicorn.show()
            time.sleep(0.5)
            s.update()
            if s.detect_collision():
                handle_it()
            s.clear()
    except KeyboardInterrupt:
        s.clear()

def handle_it():
    v3 = v1 + v2
    part3 = ParticleObject(s.physics_objects[0].x,s.physics_objects[0].y,v3)
    s.physics_objects.remove[0]

test6()