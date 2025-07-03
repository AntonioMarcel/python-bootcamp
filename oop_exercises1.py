# 1 
import math

class Line:
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    # Distância entre dois pontos na reta
    def distance(self):
        return math.sqrt(
            (self.coor2[0] - self.coor1[0]) ** 2 + (self.coor2[1] - self.coor1[1]) ** 2
        )
    
    # Inclinação da reta
    def slope(self):
        return (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])

li = Line((3,2),(8,10))
d = li.distance()
slope = li.slope()

print(d)
print(slope)

# 2
class Cylinder:
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        vol = math.pi * self.radius**2 * self.height 
        # Round to 1 dec
        return math.floor(vol*10)/10 

    def surface_area(self):
         s_area = 2 * math.pi * self.radius * (self.radius + self.height)
         # Round to 1 dec
         return math.floor(s_area*10)/10 

c = Cylinder(2,3)
vol = c.volume()
s_area = c.surface_area() 
print(vol)
print(s_area)