#a scene is composed of objects
from AbstractObject import *

try:
    import unicornhathd as unicorn
    print("unicorn hat hd detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd as unicorn
    


class scene():

    def __init__(self, gravity, friction) -> None:
        self.gravity = gravity
        self.friction = friction
        self.physics_objects = []
        self.static_objects = []
#wassup bro
#hewwo

    def create_physics_object(self, physics_object): #adds a physics object to a scene
        self.physics_objects.append(physics_object)
    
    def create_static_object(self, static_object): #adds a static object to a scene
        self.static_objects.append(static_object)

    def render_scene(self): #renders all objects in a scene
        unicorn.clear()
        for object in self.physics_objects:
            object.render()
        for object in self.static_objects:
            object.render()
        unicorn.show()
    
    def clear(self):
        for i in range(0,16):
            for j in range(0,16):
                unicorn.set_pixel(i,j,0,0,0)


    

