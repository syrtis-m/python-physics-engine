import sys
import random
from timeit import default_timer as timer

sys.path.append('../python-physics-engine')
sys.path.append('../python-physics-engine/objects')
from objects.ParticleObject import *
from scene import *
from collision_manager import CollisionManager
u_width, u_height = unicorn.get_shape()

ANIMATION_SPEED = 0.15
MAX_PARTICLES = 10
WAIT_TIME = 2
COUNT = 0 
N = 7 # number of sims to run


def setup():
    s = scene(forcesZeroG)

    n = random.randint(2,MAX_PARTICLES)
    for i in range(0,n):
        x = random.randint(0,15)
        y = random.randint(0,15)
        v = [random.randint(-2,2),random.randint(-2,2)]
        r = 255*random.randint(0,1)
        g = 255*random.randint(0,1)
        b = 255*random.randint(0,1)
        obj = ParticleObject(x,y,v,(r,g,b))
        s.create_physics_object(obj)

    demo_c(s)


def demo_c(s):
    start = timer()
    end = timer()

    try:
        while ((end-start) < float(WAIT_TIME) and (not s.isFinished())):
            s.render()
            unicorn.show()
            time.sleep(ANIMATION_SPEED)
            s.update()
            s.clear()
            end = timer()
        incr()
        if COUNT > N:
            return
        setup()
    except KeyboardInterrupt:
        s.clear()

def incr():
    global COUNT 
    COUNT += 1
#setup()