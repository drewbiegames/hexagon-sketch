#Hexagon Grid by ShadySyntax
from hex import Hex

class HexGrid:
    def __init__(self, wide, high, hex_size):
        self.grid = []
        self.wide = wide
        self.high = high
        self.hex_size = hex_size
    
    def initialise(self):
        for x in range(self.wide):
            self.grid.append([])
            for y in range(self.high):
                hex = Hex(x, y, self.hex_size)
                self.grid[x].append(hex)
        
    def show(self):
        for row in self.grid:
            for node in row:
                node.show()
                
    def __str__(self):
        return "The grid has {} hexagons, is {} hexagons wide and {} hexagons high.\nThe size of each hexagon is {}."
    
