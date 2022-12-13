import math

class Vector: #From Day 9
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Vector) and __o.x == self.x and __o.y == self.y

    def __hash__(self) -> int:
        return (self.x + self.y + 1) * (self.x + self.y) // 2 + self.y #Cantor Pairing Function

    def __add__(self, v2):
        x = self.x + v2.x
        y = self.y + v2.y
        return Vector(x,y)

    def __iadd__(self, v2):
        self.x += v2.x
        self.y += v2.y
        return self

    def __sub__(self, v2):
        x = self.x - v2.x
        y = self.y - v2.y
        return Vector(x,y)

    def __isub__(self, v2):
        self.x -= v2.x
        self.y -= v2.y
        return self

    def __len__(self):
        return int(math.sqrt(self.x ** 2 + self.y ** 2))

    def __str__(self):
        return f'({self.x},{self.y})'
    
    def __repr__(self) -> str:
        return self.__str__()

    def copy(self):
        return Vector(self.x,self.y)

    def unitize(self):
        if abs(self.x) > 1:
            self.x //= abs(self.x)
        if abs(self.y) > 1:
            self.y //= abs(self.y)

    def unit(self):
        newVect = self.copy()
        newVect.unitize()
        return newVect


class Cave:
    def __init__(self, minX, maxX, maxY) -> None:
        self.minX = minX
        self.maxX = maxX
        self.maxY = maxY
        self.grid = [['.']*(maxX-minX+1) for _ in range(maxY+1)]
        self.start = self.normalizeVector(Vector(500,0))
        
    def normalizeVector(self, vect: Vector):
        return Vector(vect.x - self.minX, vect.y)
        
    def placeRock(self, location: Vector):
        loc = self.normalizeVector(location)
        self.grid[loc.y][loc.x] = '#'
    
    def placeLine(self, start: Vector, end: Vector):
        increment = (end - start).unit()
        current = start.copy()
        while current != end:
            self.placeRock(current)
            current += increment
        self.placeRock(current)
    
    def __repr__(self) -> str:
        return '\n'.join([f'{i} '+''.join(self.grid[i]) for i in range(len(self.grid))])

    def dropSand(self): # Returns true if sand settled. False if it fell out the bottom. (and places sand)
        sand = self.start.copy()
        while True:
            if self.grid[sand.y+1][sand.x] == '.':
                sand.y += 1
            elif self.grid[sand.y+1][sand.x-1] == '.': #Left
                sand.y += 1
                sand.x -= 1
            elif self.grid[sand.y+1][sand.x+1] == '.': #Right
                sand.y += 1
                sand.x += 1
            else:
                self.grid[sand.y][sand.x] = 'O' #Settled
                return True
            if sand.y >= self.maxY: #Fell out the bottom
                return False

    def addFinalPath(self):
        sand = self.start.copy()
        while True:
            self.grid[sand.y][sand.x] = '~'
            if self.grid[sand.y+1][sand.x] == '.':
                sand.y += 1
            elif self.grid[sand.y+1][sand.x-1] == '.': #Left
                sand.y += 1
                sand.x -= 1
            elif self.grid[sand.y+1][sand.x+1] == '.': #Right
                sand.y += 1
                sand.x += 1
            else:
                self.grid[sand.y][sand.x] = 'O' #Settled
                break
            if sand.y >= self.maxY: #Fell out the bottom
                break



with open('input.txt', 'r') as f:
    rocks_str = f.read().split('\n')[:-1]


minX = 1_000_000
maxX = 0
maxY = 0

def formingStep(coord_str):
    global minX, maxX, maxY
    x,y = coord_str.split(',')
    coord = Vector(int(x),int(y))
    if coord.x < minX:
        minX = coord.x
    if coord.x > maxX:
        maxX = coord.x
    if coord.y > maxY:
        maxY = coord.y
    return coord

rocks = [[formingStep(coord) for coord in structure.split(' -> ')] for structure in rocks_str]

cave = Cave(minX, maxX, maxY)

for structure in rocks:
    for i in range(1, len(structure)):
        cave.placeLine(structure[i-1], structure[i])

# The cave has now been populated with its rocks

total_rested = 0
while cave.dropSand():
    total_rested += 1

cave.addFinalPath()
print(cave)
print(total_rested)

