import sys
import random
from timeit import default_timer as timer

sys.path.append('../python-physics-engine')
sys.path.append('../python-physics-engine/objects')
from objects.ParticleObject import *
from scene import *
from collision_manager import CollisionManager
u_width, u_height = unicorn.get_shape()


def setup():
    cm = CollisionManager()
    s = scene(cm,0,0,0)

    n = random.randint(2,30)
    for i in range(0,n):
        x = random.randint(0,15)
        y = random.randint(0,15)
        v = [random.randint(-2,2),random.randint(-2,2)]
        r = 255*random.randint(0,1)
        g = 255*random.randint(0,1)
        b = 255*random.randint(0,1)
        obj = ParticleObject(x,y,v,(r,g,b))
        s.create_physics_object(obj)

    demo(s)


def demo(s):
    start = timer()
    end = timer()

    try:
        while ((end-start) < float(2) and (not s.isFinished())):
            s.render()
            unicorn.show()
            time.sleep(0.1)
            s.update()
            s.clear()
            end = timer()
        setup()
    except KeyboardInterrupt:
        s.clear()

setup()