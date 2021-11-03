# Hexagon class by Shady Syntax
class Hex:
    _sqrt_3 = sqrt(3)
    
    def __init__(self, x, y, s):
        # x and y are the indices for the hexagon
        # s is the length between the centre and one vertex
        self.x_index = x
        self.y_index = y
        self.size = s
        self.w = 2 * s
        self.h = self._sqrt_3 * s
        self.position = (self.x_index * (self.w * 0.75), 
                        self.y_index * self.h - (0 if self.x_index % 2 else self.h / 2)) 
        self.vertices = [self._calculate_vertex(v) for v in range(6)]
        self.colour = (random(255), random(255), random(255))


    def show(self):
        push()
        fill(self.colour[0], self.colour[1], self.colour[2])
        translate(self.position[0], self.position[1])
        beginShape()
        for vert in self.vertices:
            vertex(vert[0], vert[1])
        endShape()
        pop()

    def _calculate_vertex(self, i):
        #i is the index of the vertex
        angle_rad = PI / 180 * (60 * i)
        return (self.size * cos(angle_rad), 
            self.size * sin(angle_rad))
        
    def __str__(self):
        return "x: {} y: {} s: {} w: {} h: {}".format(self.x,self.y,self.s,self.w,self.h)
