from AbstractObject import *

  

class StaticObject(AbstractObject): #staticobject means it's a object which physics deos not effect. a line.
    def __init__(self, color, object_specific_setup) -> None:
        self.type = "simple" #used in scene collision detection logic
        self.xy = []
        self.velocity = [0,0]
        self.r = color[0]
        self.g = color[1]
        self.b = color[2]
        self.dimensions = object_specific_setup #in this case, object_specific_setup is a tuple of format ((x,y),(x,y))
        self.genPhysicsShape()#this func sets self.x and self.y to be at every point
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self.smod = 1
        self.d = 0
        self.slope = 0

    def xymath(self): #does all the math necessary to set up render() or genPhysicsShape() to draw a line between two points
        x1, y1 = self.dimensions[0][0], self.dimensions[0][1]
        x2, y2 = self.dimensions[1][0], self.dimensions[1][1]

        a = (x1,y1)
        b = (x2,y2)

        smod = 1

        if (x1 > x2) and (y1 >= y2): #flip points if upward sloping line but points are in wrong place
            x2, y2 = a[0], a[1]
            x1, y1 = b[0], b[1]
        elif (y1 < y2) and (x1 != x2): #deal with downward sloping lines or points in the wrong place
            smod = -1
            if (x1>x2):
                x2, y2 = a[0], a[1]
                x1, y1 = b[0], b[1]
        elif (y1 > y2) and (x1 <= x2):
            x2, y2 = a[0], a[1]
            x1, y1 = b[0], b[1]
            
        run = 1

        try:
            slope = abs((y2 - y1)) / abs((x2 - x1))
        except ZeroDivisionError:
            slope = 1
            run = 0

        slope = slope * smod #adjust for downward sloping lines by mult by -1

        dist = lambda p1, p2: math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

        d = int(dist((x1, y1),(x2, y2)))
        
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.smod = smod
        self.d = d
        self.slope = slope
        self.run = run

    def render(self):
        self.xymath()

        x=self.x1
        y=self.y1

        for i in range(self.d+1):
            if ((x>15) or (y>15)):
                pass
            elif ((x<0) or (y<0)):
                pass
            else:
                unicorn.set_pixel(int(x),int(y), self.r, self.g, self.b)
            x = x + self.run
            y = y + self.slope

    

    def genPhysicsShape(self):
        self.xymath()
        
        x=self.x1
        y=self.y1
        print(self.slope)

        for i in range(self.d+1):
            if ((x>15) or (y>15)):
                pass
            elif ((x<0) or (y<0)):
                pass
            else:
                self.xy.append((int(x), int(y), self.slope))
            x = x + self.run
            y = y + self.slope        

    
    def updatePosition(self):
        return
    
    def isOutOfBounds(self):
        return False #static objects are never destroyed

    def addForce(self, force: tuple): #this should result in no force being added
        return
