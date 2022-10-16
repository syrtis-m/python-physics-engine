#a scene is composed of objects
import sys
sys.path.append('../python-physics-engine/objects')
from objects.AbstractObject import *
import math
from collision_manager import CollisionManager

try:
    import unicornhathd as unicorn
    print("unicorn hat hd detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd as unicorn


#forces options for scene()
forcesDefault = {
  "gravity": 0.5,
  "friction": 0.5,
  "COR": 1
}

forcesZeroG = {
    "gravity" : 0,
    "friction" : 0.5,
    "COR" : 1

}
    

class scene():
    #the scene class manages all objects in a scene, as well as global physics values such as friction and gravity
    #scenes take a dict of forces - examples above


    def __init__(self, forces : dict) -> None:
        #config
        self.gravity = forces["gravity"]
        self.friction = forces["friction"]
        self.COR = forces["COR"] #coefficient of restitution. needed for calculating collisions against static object
        self.cm = CollisionManager()

        #state tracking
        self.physics_objects = []
        self.static_objects = []
        self.staticPositions = [] #positions of each point of each static object
        self.finished = False
        self.time = 0 #global counter for force calculations  


##-----scene-object manipulaters-----##
    def create_physics_object(self, physics_object): #adds a physics object to a scene
        self.physics_objects.append(physics_object)

    def destroy_physics_object(self, physics_object): #removes physics object from scene
        self.physics_objects.remove(physics_object)
    
    def create_static_object(self, static_object): #adds a static object to a scene
        self.static_objects.append(static_object)
        self.setUpStaticCollision() #find all static positions and keep track of them

    def destroy_static_object(self, static_object): #removes a static object from a scene
        self.static_objects.remove(static_object)
        self.setUpStaticCollision() #find all static positions and keep track of them


##-----core graphics render functionality-----##
    def render(self): #renders all objects in a scene
        self.clear()
        for object in self.physics_objects:
            object.render()
        for object in self.static_objects:
            object.render()
        unicorn.show()

##-----core physics update functionality-----##
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
                    self.finished = True
                    return
            magnitudes.append(math.sqrt(object.velocity[0]**2+object.velocity[1]**2))

        #only check collision for physics objects if there are physics objects in the scene
        if self.physics_objects:
            # check collision relative to max velocity 
            # (i.e., the faster a particle is moving the farther away detection radius must be)
            collided, colliders  = self.detectCollision(max(magnitudes)) 
            if collided:
                # print("algo detected collision -- ouch!")
                for obj1,obj2 in colliders:
                    self.create_physics_object(self.cm.phys_phys_handler(obj1,obj2))
                    # for some reason the collision alg will output objs which don't exist in the list
                    # which causes errors. I wrapped this in ifs to prevent this, 
                    # but need to look into it.
                    if obj1 in self.physics_objects:
                        self.destroy_physics_object(obj1)
                    if obj2 in self.physics_objects:
                        self.destroy_physics_object(obj2) 
        #only check collision for static objects if there are static objects in the scene
        if self.static_objects:
          collidedStatic, phys, stat = self.detectStaticCollision(max(magnitudes))
          if collidedStatic:
              self.create_physics_object(self.cm.phys_stat_handler(phys,stat, self.gravity, self.friction, self.COR))
              self.destroy_physics_object(phys)


##-----collision-----##
    # https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer-algorithm/
    # determine if any object is within z distance from another object
    # returns a bool if collision detected or not, and if so the two objects which collided 
    def detectCollision(self, maxVelocity) -> bool: 
        def dist(obj1, obj2):
            return math.sqrt((obj1.x-obj2.x)**2+(obj1.y-obj2.y)**2)

        collisions = []
        n = len(self.physics_objects)
        #brute force find distance betweeen points    
        for i in range(n):
            for j in range(i + 1, n):
                obj1 = self.physics_objects[i]
                obj2 = self.physics_objects[j]
                d = dist(obj1, obj2)
                if d <= maxVelocity:
                    proj_pos_1 = [obj1.x+obj1.velocity[0],obj1.y+obj1.velocity[1]]
                    proj_pos_2 = [obj2.x+obj2.velocity[0],obj2.y+obj2.velocity[1]]
                    if self.compareProjection(proj_pos_1, [obj2.x,obj2.y]) \
                        or self.compareProjection(proj_pos_2, [obj1.x,obj1.y]):
                        collisions.append([obj1, obj2]) 
                """
                if d < min_val:
                    min_val = d
                    if min_val < maxVelocity:
                        collisions.append([obj1, obj2])
                        print(collisions)
                """
        if collisions:                
            return True, collisions
        else:
            return False, None
    
    def setUpStaticCollision(self): #run to set up all static positions in the scene
        staticPositions= []
        for object in self.static_objects:
            for obj in object.xy:
                #add slope of line
                staticPositions.append([obj[0], obj[1], obj[2]]) #get all positions of all static objects. treat these as fixed points in the scene
        self.staticPositions = staticPositions #store all static positions

    def detectStaticCollision(self, maxVelocity) -> bool:
        #compare all particles to all static positions
        def dist(obj1, obj2X, obj2Y):
            return math.sqrt((obj1.x-obj2X)**2+(obj1.y-obj2Y)**2)
        positions = []
        for object in self.physics_objects:
            positions.append([object.x, object.y])
            
        min_val = float('inf') 
        n = len(self.physics_objects)
        staticsCount = len(self.staticPositions)
        #brute force find distance betweeen points    
        for i in range(n):
            for j in range(i, staticsCount):
                obj1 = self.physics_objects[i]
                obj2 = self.staticPositions[j]
                obj2X = self.staticPositions[j][0]
                obj2Y = self.staticPositions[j][1]


                d = dist(obj1, obj2X, obj2Y)
                if d < min_val:
                    min_val = d
        if min_val < maxVelocity:
            return True, obj1, obj2
        else:
            return False, None, None        


##-----misc-----##
    def isFinished(self): #basic getter for flag data
        if self.finished:
            return True
        else:
            return False
    
    def clear(self): #clears a scene because unicorn.clear() doesn't work
        for i in range(0,16):
            for j in range(0,16):
                unicorn.set_pixel(i,j,0,0,0)

    def sign(x):
        if x>0:
            return 1
        elif x==0:
            return 0
        else:
            return -1
    
    # helper function to compare particle projection to given position,
    # for purpose of determining collisions.
    def compareProjection(self, proj_pos: tuple, pos):
        if proj_pos < pos or proj_pos > pos or proj_pos == pos:
            return True
        return False

            



