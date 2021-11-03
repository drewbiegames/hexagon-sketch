# Hexagon Grid Sketch by Shady Syntax
from grid import HexGrid

GRID = HexGrid(10, 10, 25)

def setup():
    size(500, 500)
    noLoop()
    GRID.initialise()


def draw():
    push()
    translate(25,50)
    GRID.show()
    pop()
