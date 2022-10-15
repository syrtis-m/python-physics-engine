# import stuff

from render import *
import test_1
import test_2
import test_3
import test_4

def test():
    unicorn.set_pixel(1, 1, 235, 64, 52)
    print("shouldve shown")
    unicorn.show()

waittime = 8

while (True):
    test_1.test1(waittime)
    test_2.test2(waittime)
    test_3.test3(waittime)
    #test_4.test4(waittime)
#physics render loop
#while (True):
#    render_objects(objects)