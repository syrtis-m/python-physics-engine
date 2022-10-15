# import stuff
import time
from timeit import default_timer as timer
from scene import *



#this try/except from github.com/jayniz/unicorn-hat-sim
try:
    import unicornhathd as unicorn
    print("unicorn hat hd detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd as unicorn




# collision handler. will either display simple 'explosion' animation or
# a particle moving off in another direction
def collision(scene):
    """"
    clear()
    unicorn.set_pixel(7,8,255,0,0)
    unicorn.set_pixel(8,7,255,0,0)
    unicorn.set_pixel(7,6,255,0,0)
    unicorn.set_pixel(6,7,255,0,0)
    unicorn.show()
    time.sleep(0.5)
    clear()
    unicorn.set_pixel(7,9,255,0,0)
    unicorn.set_pixel(9,7,255,0,0)
    unicorn.set_pixel(7,5,255,0,0)
    unicorn.set_pixel(5,7,255,0,0)
    unicorn.show()
    time.sleep(0.5)
    clear()
    """
    scene.clear()
    for i in range(7,16):
        unicorn.set_pixel(7,i,255,0,0)
        unicorn.show()
        time.sleep(0.10)
        scene.clear()

def test3(waittime):
    #display 2 pixels moving across board
    scene = scene(0,0)

    start = timer()
    end = timer()
    try:
        while((end-start) < float(waittime)):
            for i in range(0,16):
                unicorn.set_pixel(i,7,255,255,255)
                unicorn.set_pixel(15-i,7,255,255,255)
                if i == 15-i+1:
                    collision(scene)
                    break
                unicorn.show()
                time.sleep(0.25)
                scene.clear()
            end = timer()
    except KeyboardInterrupt:
        scene.clear()
