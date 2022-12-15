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

def manhattanDistance(start, end):
    return abs(end.x - start.x) + abs(end.y - start.y)


with open('input.txt', 'r') as f:
    sensors = f.read().splitlines(keepends=False)


# row = 10
row = 2_000_000

beaconless = set()

for sensor in sensors:
    parts = sensor.split(': ')
    location_parts = parts[0].split(', ')
    location = Vector(int(location_parts[0][location_parts[0].index('x=')+2:]), int(location_parts[1][2:]))
    beacon_parts = parts[1].split(', ')
    beacon = Vector(int(beacon_parts[0][beacon_parts[0].index('x=')+2:]), int(beacon_parts[1][2:]))

    distance_to_beacon = manhattanDistance(location, beacon)
    # print(f"Distance from sensor {location} to beacon {beacon} is", distance_to_beacon)

    vert_to_row = abs(row - location.y)
    # print("Distance to row is", vert_to_row)
    if vert_to_row <= distance_to_beacon:
        start = Vector(location.x - (distance_to_beacon - vert_to_row), row)
        finalX = location.x + (distance_to_beacon - vert_to_row)
        while start.x <= finalX:
            if start != beacon:
                beaconless.add(start.copy())
                # print("Added", start)
            start.x += 1
        # print()
    
# print(beaconless)
print(len(beaconless))


