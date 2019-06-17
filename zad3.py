import math

class Linija:
    def __init__(self, x, y):
        self.x1 = x[0]
        self.y1 = x[1]
        self.x2 = y[0]
        self.y2 = y[1]
    
    def slope(self):
        return ((self.y2-self.y1)/(self.x2-self.x1))

    def distanca(self):
        return math.sqrt(pow((self.x2-self.x1),2)+pow((self.y2-self.y1),2))

lin=Linija((3,2),(8,10))
print(lin.slope())
print(lin.distanca())
