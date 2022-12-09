import math

class Vector:
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

    def copy(self):
        return Vector(self.x,self.y)



with open("input.txt", "r") as f:
    steps = f.read().split('\n')[:-1]
        

visited_set = {Vector(0,0)}
head = Vector(0,0)
tail = Vector(0,0)


def move(xDir, yDir, times):
    global visited_set, head, tail
    for _ in range(times):
        if xDir != 0:
            head.x += xDir
            if len(head - tail) > 1:
                tail.x += xDir
                tail.y = head.y
                visited_set.add(tail.copy())
        if yDir != 0:
            head.y += yDir
            if len(head - tail) > 1:
                tail.y += yDir
                tail.x = head.x
                visited_set.add(tail.copy())

def doSteps(steps):
    for step in steps:
        direction, times = step.split(' ')
        if direction == 'R':
            move(1, 0, int(times))
        if direction == 'U':
            move(0, 1, int(times))
        if direction == 'L':
            move(-1, 0, int(times))
        if direction == 'D':
            move(0, -1, int(times))

doSteps(steps)

print(len(visited_set))