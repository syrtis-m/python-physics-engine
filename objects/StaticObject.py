from AbstractObject import *

  

class StaticObject(AbstractObject): #staticobject means it's a object which physics deos not effect. a line.
    def __init__(self, x, y, color, object_specific_setup) -> None:
        self.x = x
        self.y = y
        self.velocity = [0,0]
        self.r = color[0]
        self.g = color[1]
        self.b = color[2]
        self.dimensions = object_specific_setup #in this case, object_specific_setup is a tuple of format ((x,y),(x,y))

    def render(self):

        dist = lambda p1, p2: math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

        x1 = self.dimensions[0][0]
        y1 = self.dimensions[0][1]
        x2 = self.dimensions[1][0]
        y2 = self.dimensions[1][1]

        a = (x1,y1)
        b = (x2,y2)
        if y1>y2:
            x2, y2 = a[0], a[1]
            x1, y1 = b[0], b[1]

        run = 1

        try:
            slope = (y2 -y1) / (x2 - x1)
        except ZeroDivisionError:
            slope = 1
            run = 0

        d = int(dist((x1,y1),(x2,y2)))

        x=x1
        y=y1

        for i in range(d):
            if ((x>15) or (y>15)):
                break
            unicorn.set_pixel(int(x),int(y), self.r, self.g, self.b)
            x = x + run
            y = y + slope

    def updatePosition(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]
    
    def isOutOfBounds(self):
        return False #static objects are never destroyed