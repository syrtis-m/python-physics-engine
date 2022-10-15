# import stuff
import time

#this try/except from github.com/jayniz/unicorn-hat-sim
try:
    import unicornhathd as unicorn
    print("unicorn hat hd detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd as unicorn

#custon clear function because unicorn.clear() doesn't work for the sim :)
def clear():
    for i in range(0,16):
        for j in range(0,16):
            unicorn.set_pixel(i,j,0,0,0)

#display pixel moving across board
try:
    while(True):
        for i in range(0,16):
            unicorn.set_pixel(i,0,255,255,255)
            unicorn.show()
            time.sleep(0.5)
            clear()
except KeyboardInterrupt:
    clear()
