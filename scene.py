#a scene is composed of objects
from http.client import PARTIAL_CONTENT
import sys
from xmlrpc.client import Boolean
sys.path.append('../python-physics-engine/objects')
from objects.AbstractObject import *
import math
from collision_manager import CollisionManager

try:
    import unicornhathd as unicorn
    print("unicorn hat hd detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd as unicorn
    


class scene():
    #the scene class manages all objects in a scene, as well as global physics values such as friction and gravity

    def __init__(self, cm: CollisionManager, gravity, friction) -> None:
        self.cm = cm
        self.gravity = gravity
        self.friction = friction
        self.physics_objects = []
        self.static_objects = []

    def create_physics_object(self, physics_object): #adds a physics object to a scene
        self.physics_objects.append(physics_object)

    def destroy_physics_object(self, physics_object): #removes physics object from scene
        self.physics_objects.remove(physics_object)
    
    def create_static_object(self, static_object): #adds a static object to a scene
        self.static_objects.append(static_object)

    def destroy_static_object(self, static_object): #removes a static object from a scene
        self.static_objects.remove(static_object)

    def render(self): #renders all objects in a scene

        self.clear()
        for object in self.physics_objects:
            object.render()
        for object in self.static_objects:
            object.render()
        unicorn.show()


    def update(self):
        if (self.gravity > 0):
            for object in self.physics_objects:
                object.addForce((0,self.gravity))

        magnitudes = []
        for object in self.physics_objects:
            object.updatePosition()
            if object.isOutOfBounds():
                self.destroy_physics_object(object)
                if not self.physics_objects: #if no more objects, end the sim
                    unicorn.off()
            magnitudes.append(math.sqrt(object.velocity[0]**2+object.velocity[1]**2))
        collided, obj1, obj2  = self.detectCollision(max(magnitudes))
        if collided:
            print("algo detected collision -- ouch!")
            self.create_physics_object(self.cm.phys_phys_handler(obj1,obj2))
            self.destroy_physics_object(obj1)
            self.destroy_physics_object(obj2) 


    # https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer-algorithm/
    def detectCollision(self, maxVelocity) -> Boolean: #determine if any object is within z distance from another object
        def dist(obj1, obj2):
            return math.sqrt((obj1.x-obj2.x)**2+(obj1.y-obj2.y)**2)
        positions = []
        for object in self.physics_objects:
            positions.append([object.x, object.y])
            
        min_val = float('inf') 
        n = len(self.physics_objects)
        #brute force find distance betweeen points    
        for i in range(n):
            for j in range(i + 1, n):
                obj1 = self.physics_objects[i]
                obj2 = self.physics_objects[j]
                d = dist(obj1, obj2)
                if d < min_val:
                    min_val = d
        if min_val < maxVelocity:
            #self.cm.phys_phys_handler(obj1,obj2)
            return True, obj1, obj2
        else:
            return False, None, None

        

    def clear(self): #clears a scene because unicorn.clear() doesn't work great
        for i in range(0,16):
            for j in range(0,16):
                unicorn.set_pixel(i,j,0,0,0)



