from AbstractObject import *

  

class StaticObject(AbstractObject): #staticobject means it's a object which physics deos not effect. a line.
    def __init__(self, color, object_specific_setup) -> None:
        self.xy = []
        self.velocity = [0,0]
        self.r = color[0]
        self.g = color[1]
        self.b = color[2]
        self.dimensions = object_specific_setup #in this case, object_specific_setup is a tuple of format ((x,y),(x,y))
        self.genPhysicsShape()#this func sets self.x and self.y to be at every point




    def render(self):
        x1, y1 = self.dimensions[0][0], self.dimensions[0][1]
        x2, y2 = self.dimensions[1][0], self.dimensions[1][1]

        a = (x1,y1)
        b = (x2,y2)

        if (x1>x2) and (y1 >= y2): #flip points if upward sloping line but points are in wrong place
            x2, y2 = a[0], a[1]
            x1, y1 = b[0], b[1]
            smod = 1
        
        if (y1 < y2): #deal with downward sloping lines or points in the wrong place
            smod = -1
            if (x1>x2):
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

        d = int(dist((x1,y1),(x2,y2)))

        x=x1
        y=y1

        for i in range(d):
            if ((x>15) or (y>15)):
                break
            unicorn.set_pixel(int(x),int(y), self.r, self.g, self.b)
            x = x + run
            y = y + slope

    def genPhysicsShape(self):
        x1, y1 = self.dimensions[0][0], self.dimensions[0][1]
        x2, y2 = self.dimensions[1][0], self.dimensions[1][1]

        a = (x1,y1)
        b = (x2,y2)

        if (x1>x2) and (y1 >= y2): #flip points if upward sloping line but points are in wrong place
            x2, y2 = a[0], a[1]
            x1, y1 = b[0], b[1]
            smod = 1
        
        if (y1 < y2): #deal with downward sloping lines or points in the wrong place
            smod = -1
            if (x1>x2):
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

        d = int(dist((x1,y1),(x2,y2)))

        x=x1
        y=y1

        for i in range(d):
            if ((x>15) or (y>15)):
                break
            self.xy.append((int(x), int(y), slope))
            x = x + run
            y = y + slope        

    def updatePosition(self):
        return
    
    def isOutOfBounds(self):
        return False #static objects are never destroyed

    def addForce(self, force: Tuple): #this should result in no force being added
        return
