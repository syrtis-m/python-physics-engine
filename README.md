# python-physics-engine
[see it in action.](https://youtu.be/646AFSltmto)
built for HACK WashU 2022. 
works with a raspberry pi and a unicorn hat HD.
### dependencies
numpy, [FastLine](https://github.com/MrGolden1/FastLine)


## Inspiration

30-minute youtube videos showing off other physics engines and CSE 450A, insofar that working in Unity and on games has a similar loop of update --> render. Also, we just thought it would be neat!
What it does

Currently it is basic physics engine with static and dynamic objects, i.e., walls and balls/particles. The latter can undergo inelastic or elastic collision with static or other dynamic objects, respectively. Each demo we've prepared is rendered in real-time on the Raspberry Pi Zero and displayed on the UnicornHATHD. Our main function cycles through our progression, from displaying a single pixel to simulating a ball bouncing off multiple surfaces.

## How we built it

We used OOP to create objects, a scene, and a collision handler to handle object interaction. All code is in Python. The only packages we used were Numpy, the UnicornHATHD API (the text scroll is pulled from here, all credit to them), and FastLine, a small repo we use to calculate vector intersections for collision detection. In other words, we built the engine from (nearly) scratch, developing algorithms and rendering solutions ourselves with minimal influence from the web.
Challenges we ran into

Rendering physics demos on a 16x16 pixel board proved more difficult than we had originally thought. A lot of trouble came from being forced to render in only integers -- not floats, which is not entirely conducive to physics calculations. The collision detection was also a real pain, in part again due to the strict constraint to integers, and trade-offs between accuracy and computational efficiency. For instance, in trying to handle simultaneous collisions, we developed an O(n!) algorithm; needless to say, there's no way a Raspberry Pi Zero can handle that.
Accomplishments that we're proud of

Due to the relatively niche nature of our project, running a physics engine but also rendering it on a HAT, meant that we had to rely on our own knowledge and could not Google as much as a software dev would like. The fact that the thing works at all, and to the level it does, after only, essentially, a day of work is extremely gratifying.

## What we learned

Python, believe it or not, is not a great language for low-level computations and simulation! Go figure. Also, rendering things is hard — and rendering them on LED pixels is even harder.


## setup
- put the Unicorn Hat HD onto your raspberry pi's GPIO pins
- install unicornhathd from https://github.com/pimoroni/unicorn-hat-hd
- install FastLine `pip3 install FastLine`
- clone this repo
- run `python3 main.py` for demos
