import math

class Vect():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, inputVect):
        self.x += inputVect.x
        self.y += inputVect.y
        # Optionally, return self if you want to chain methods
        return self

    
    def __str__(self):
        return str([self.x, self.y])
    
    def unitize(self, radius=None):
        if radius is None:
            radius = 1
        c = math.sqrt(self.x**2 + self.y**2) * (1/radius)
        if c != 0:
            self.x /= c
            self.y /= c

    def multiply(self, scale):
        self.x *= scale
        self.y *= scale
        # Optionally, return self if you want to chain methods
        return self
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getMagnitude(self):
        return math.sqrt(self.y**2 + self.x**2)
    
    def getRoundX(self):
        return round(self.x)
    
    def getRoundY(self):
        return round(self.y)
    
    def squareClamp(self, clampRadius):
        if self.y >=  clampRadius: self.y =  clampRadius
        if self.y <= -clampRadius: self.y = -clampRadius
        if self.x >=  clampRadius: self.x =  clampRadius
        if self.x <= -clampRadius: self.x = -clampRadius
    
    def circularClamp(self, radius=None):
        if radius is None:
            radius = 1
        if self.getMagnitude() > radius:
            self.unitize(radius)