#bouncing ball demo with box static object
import sys
import time
sys.path.append('../python-physics-engine')
sys.path.append('../python-physics-engine/objects')

from scene import *
from objects.StaticBoxObject import StaticBoxObject
from objects.BallObject import BallObject
from timeit import default_timer as timer


def test_8_bounce2(waittime):

    forcesTest = {  
        "gravity": 0.5,
        "friction": 0.5,
        "COR": 1
    }

    s = scene(forcesTest)

    dimensions = [(15,13), (0,13), (0,15), (15,15)]
    green = (3, 255, 37)
    box = StaticBoxObject(green, dimensions)
    s.create_static_object(box)    

    s.create_physics_object(BallObject(15,0,(-0.5,0),(255,255,255)))
    
    start = timer()
    end = timer()
    while((end-start) < waittime):
        s.render()
        time.sleep(0.1)
        s.update()
        end = timer()


test_8_bounce2(5)