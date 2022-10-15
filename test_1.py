# import stuff
import numpy as np

#this try/except from github.com/jayniz/unicorn-hat-sim
try:
    import unicornhathd as unicorn
    print("unicorn hat hd detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd as unicorn

#display single pixel
try:
    while(True):
        unicorn.set_pixel(0,0,255,255,255)
        unicorn.show()
except KeyboardInterrupt:
    unicorn.clear()
