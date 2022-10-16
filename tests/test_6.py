from cgi import test
import sys
sys.path.append('../python-physics-engine')
sys.path.append('../python-physics-engine/objects')
from objects.ParticleObject import *
from scene import *
from collision_manager import CollisionManager
u_width, u_height = unicorn.get_shape()



def test6():
    #display 2 particles colliding
    """"
    def handle_it():
        v3 = [v1[0]+v2[0], v1[1]+v2[1]]
        part3 = ParticleObject(s.physics_objects[0].x,s.physics_objects[0].y,v3)
        s.create_physics_object(part3)
        s.destroy_physics_object(part1)
        s.destroy_physics_object(part2)
        print(s.physics_objects)
    """
    
    s = scene(forcesZeroG)
    v1 = [2,1]
    v2 = [-1,1] 
    part1 = ParticleObject(1,1,v1,(255,255,255))
    part2 = ParticleObject(15,1,v2,(255,255,255))

    s.create_physics_object(part1)
    s.create_physics_object(part2)

    try:
        while(True):
            s.render()
            unicorn.show()
            time.sleep(0.1)
            s.update()
            s.clear()
    except KeyboardInterrupt:
        s.clear()



test6()