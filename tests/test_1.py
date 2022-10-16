# import stuff
import numpy as np
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

def test1(waittime):
    #display single pixel
    start = timer()
    end = timer()
    try:
        while((end-start) < float(waittime)):
            unicorn.set_pixel(0,0,255,255,255)
            unicorn.show()
            end = timer()
    except KeyboardInterrupt:
        unicorn.clear()

#test1(5)