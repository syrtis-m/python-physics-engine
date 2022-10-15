# import stuff
import time
from timeit import default_timer as timer
import sys
sys.path.append('../python-physics-engine')
from scene import *


#this try/except from github.com/jayniz/unicorn-hat-sim
try:
    import unicornhathd as unicorn
    print("unicorn hat hd detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd as unicorn



def test2(waittime):
    #display pixel moving across board
    scene = scene(0,0)
    start = timer()
    end = timer()
    try:
        while((end-start) < float(waittime)):
            for i in range(0,16):
                unicorn.set_pixel(i,0,255,255,255)
                unicorn.show()
                time.sleep(0.5)
                scene.clear()
            end = timer()
            
    except KeyboardInterrupt:
        scene.clear()

