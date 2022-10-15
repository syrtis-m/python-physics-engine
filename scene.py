#a scene is composed of objects
from AbstractObject import *
import math

try:
    import unicornhathd as unicorn
    print("unicorn hat hd detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd as unicorn
    


class scene():
    #the scene class manages all objects in a scene, as well as global physics values such as friction and gravity

    def __init__(self, gravity, friction) -> None:
        self.gravity = gravity
        self.friction = friction
        self.physics_objects = []
        self.static_objects = []

    def create_physics_object(self, physics_object): #adds a physics object to a scene
        self.physics_objects.append(physics_object)
    
    def create_static_object(self, static_object): #adds a static object to a scene
        self.static_objects.append(static_object)

    def render(self): #renders all objects in a scene
        unicorn.clear()
        for object in self.physics_objects:
            object.render()
        for object in self.static_objects:
            object.render()
        unicorn.show()

    def update(self):
        for object in self.physics_objects:
            object.updateposition()
        if self.detect_collision():
            print("algo detected collision -- ouch!")

    # https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer-algorithm/
    def detect_collision(self): #determine if any object is within z distance from another object
        positions = []
        dist = lambda p1, p2: math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
        for object in self.physics_objects:
            positions.append([object.x, object.y])
            
        min_val = float('inf') 
        n = len(positions)
        #brute force find distance betweeen points    
        for i in range(n):
            for j in range(i + 1, n):
                if dist(positions[i], positions[j]) < min_val:
                    min_val = dist(positions[i],positions[j])
    
        if min_val < 1:
            return True
        
        


    def clear(self): #clears a scene because unicorn.clear() doesn't work great
        for i in range(0,16):
            for j in range(0,16):
                unicorn.set_pixel(i,j,0,0,0)


