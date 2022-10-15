#bouncing ball demo
import sys
sys.path.append('../python-physics-engine')
sys.path.append('../python-physics-engine/objects')

from scene import *
from objects.StaticObject import StaticObject
from objects.ParticleObject import ParticleObject
from objects.BallObject import BallObject


def test_7_bounce():
    s = scene(0.5, 0)
    

    s.create_static_object(StaticObject(0,0,(3, 255, 37), ((15,15),(0,15))))
    s.create_physics_object(BallObject(14,0,(-0.5,0),(255,255,255)))
    

    while(True):
        s.render()
        time.sleep(0.5)
        s.update()


test_7_bounce()