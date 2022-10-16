from StaticObject import *

class StaticBoxObject(AbstractObject):

    def __init__(self, color, object_specific_setup) -> None:
        self.type = "complex" #used in scene collision detection logic
        self.xy= []
        self.static_objects = [] #list of static objects the box is made of
        self.velocity = [0,0]
        self.r = color[0]
        self.g = color[1]
        self.b = color[2]
        self.dimensions = object_specific_setup
        self.genStaticObjects(color)
        self.genPhysicsShape()
        self.xmax = 0
        self.ymax = 0
        self.ymax = 0
        self.ymin = 0


    def genStaticObjects(self, color):
        a = self.dimensions[0]
        b = self.dimensions[1]
        c = self.dimensions[2]
        d = self.dimensions[3]

        self.static_objects.append(StaticObject(color,(a,b)))
        self.static_objects.append(StaticObject(color,(b,c)))
        self.static_objects.append(StaticObject(color,(c,d)))
        self.static_objects.append(StaticObject(color,(d,a)))

    def render(self):
        for object in self.static_objects:
            object.render()
    
    def genPhysicsShape(self):
        #need xmax etc... for fast colClip later.
        # xmax = 0
        # xmin = 0
        # ymax = 0
        # ymin = 0
        for object in self.static_objects:
            object.genPhysicsShape()
            for point in object.xy:
                self.xy.append(point)
        #         if point.x > xmax:
        #             xmax = point.x
        #         if point.x < xmin:
        #             xmin = point.y
        #         if point.y > ymax:
        #             ymax = point.y
        #         if point.y < ymin:
        #             ymin = point.y
        # self.xmax = xmax
        # self.xmin = xmin
        # self.ymax = ymax
        # self.ymin = ymin
        

    
    def updatePosition(self):
        return
    
    def isOutOfBounds(self):
        return False #static objects are never destroyed

    def addForce(self, force: tuple): #this should result in no force being added
        return