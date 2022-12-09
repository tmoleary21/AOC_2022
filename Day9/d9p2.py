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

    def __repr__(self) -> str:
        return self.__str__()

    def copy(self):
        return Vector(self.x,self.y)

    def fixMovement(self):
        if abs(self.x) > 1:
            self.x //= 2
        if abs(self.y) > 1:
            self.y //= 2



with open("input.txt", "r") as f:
    steps = f.read().split('\n')[:-1]
        

visited_set = {Vector(0,0)}
head = Vector(0,0)
tail = [Vector(0,0) for _ in range(9)]

def moveTail(tailIndex):
    global visited_set, tail
    toParent = tail[tailIndex-1] - tail[tailIndex]
    if(len(toParent) > 1):
        toParent.fixMovement()
        tail[tailIndex] += toParent
        if tailIndex != len(tail)-1:
            moveTail(tailIndex + 1)
        else:
            visited_set.add(tail[tailIndex].copy())

def moveHead(xDir, yDir, times):
    global visited_set, head, tail
    for _ in range(times):
        if xDir != 0:
            head.x += xDir
            if len(head - tail[0]) > 1:
                tail[0].x += xDir
                tail[0].y = head.y
                moveTail(1)
        if yDir != 0:
            head.y += yDir
            if len(head - tail[0]) > 1:
                tail[0].y += yDir
                tail[0].x = head.x
                moveTail(1)


def doSteps(steps):
    for step in steps:
        direction, times = step.split(' ')
        if direction == 'R':
            moveHead(1, 0, int(times))
        if direction == 'U':
            moveHead(0, 1, int(times))
        if direction == 'L':
            moveHead(-1, 0, int(times))
        if direction == 'D':
            moveHead(0, -1, int(times))

doSteps(steps)

print(len(visited_set))