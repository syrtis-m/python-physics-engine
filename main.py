# import stuff
from tests.test_1 import test1
from tests.test_2 import test2
from tests.test_3 import test3
from tests.test_4 import test4
from tests.test_5 import test5
from tests.test_6 import test6
from tests.test_7_bounce import test_7_bounce
from tests.simultaneous_collision_demo import demo
from tests.simultaneous_collision_demo_2 import demo2
from tests.collision_demo import setup
from Text import *

waittime = 4

unicorn.clear()

t = Text(["Test 1"])
t.display()
test1(waittime-2)

t = Text(["Test 2"])
t.display()
test2(waittime)

t = Text(["Time for something more interesting!","Test 3"])
t.display()
test3(waittime)

t = Text(["Test 4"])
t.display()
test6(waittime)

t = Text(["Let's step it up. Time for some actual physics!","Simultaneous collision demos"])
t.display()
demo(waittime)
demo2(waittime)

t = Text(["Putting it all together: random, real-time collisions"])
t.display()
setup()

t = Text(["Scaling up, we move from particle collisions to a bouncing ball"])
t.display()
# ball demos go here