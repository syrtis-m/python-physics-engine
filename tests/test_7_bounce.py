#bouncing ball demo
import sys
sys.path.append('../python-physics-engine')
sys.path.append('../python-physics-engine/objects')

from scene import *
from objects.StaticObject import StaticObject
from objects.ParticleObject import ParticleObject

def test_7_bounce():
    s = scene(9.8, 0)
    s.create_static_object(StaticObject(0,0,(3, 255, 37), ((15,15),(15,0))))
    


    while(True):
        s.render()
        time.sleep(0.5)
        s.update()
        s.clear()


test_7_bounce()