#bouncing ball demo
import sys
import time
sys.path.append('../python-physics-engine')
sys.path.append('../python-physics-engine/objects')

from scene import *
from objects.StaticObject import StaticObject
from objects.ParticleObject import ParticleObject
from objects.BallObject import BallObject
from timeit import default_timer as timer


def test_7_bounce(waittime):

    forcesTest = {
        "gravity": 0.5,
        "friction": 0.5,
        "COR": 1
    }

    s = scene(forcesTest)

    green = (3, 255, 37)
    
    s.create_static_object(StaticObject(green, ((15,15),(0,15)))) #flat surface @ h=15
    #s.create_static_object(StaticObject(green, ((15,12),(0,12)))) #flat surface @ h=12

    #s.create_static_object(StaticObject(green, ((15,0),(0,15)))) #down left
    #s.create_static_object(StaticObject(green, ((15,13),(0,15)))) #down left
    s.create_static_object(StaticObject(green, ((10,15),(0,4)))) #test weird surface
    ## TODO fix

    s.create_physics_object(BallObject(14,0,(-.5,0),(255,255,255)))
    
    start = timer()
    end = timer()
    while((end-start) < waittime):
        s.render()
        time.sleep(0.1)
        s.update()
        end = timer()

test_7_bounce(5)

