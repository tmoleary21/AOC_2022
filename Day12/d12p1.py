
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getChildren(self):
        return [Point(self.x+1, self.y), Point(self.x, self.y+1), Point(self.x-1, self.y), Point(self.x, self.y-1)]
    def inBounds(self, heatmap):
        return self.y >= 0 and self.y < len(heatmap) and self.x >= 0 and self.x < len(heatmap[self.y])
    def __repr__(self) -> str:
        return f'({self.x},{self.y})'


with open("input.txt", "r") as f:
    heatmap = f.read().split('\n')[:-1]


distances = [[-1] * len(row) for row in heatmap]

def findStart():
    global heatmap
    for i in range(len(heatmap)):
        for j in range(len(heatmap[i])):
            if heatmap[i][j] == 'S':
                return Point(j,i)
    return -1 #Should not happen

def climbable(node, child):
    child_let = 'z' if heatmap[child.y][child.x] == 'E' else heatmap[child.y][child.x]
    node_let = 'a' if heatmap[node.y][node.x] == 'S' else heatmap[node.y][node.x]
    difference = ord(child_let) - ord(node_let)
    return difference <= 1

def BFS():
    global heatmap, distances, queue
    while len(queue) > 0:
        node = queue.pop(0)
        if heatmap[node.y][node.x] == 'E':
            return distances[node.y][node.x]
        for child in node.getChildren():
            if child.inBounds(heatmap) and climbable(node, child) and (distances[child.y][child.x] > distances[node.y][node.x] + 1 or distances[child.y][child.x] == -1):
                    distances[child.y][child.x] = distances[node.y][node.x] + 1
                    queue.append(child)
    return -1

start = findStart()
queue = [start]
distances[start.y][start.x] = 0
shortest_distance = BFS()


for row in distances:
    print(' '.join(list(map(str, row))))

print()
print(shortest_distance)

# print(heatmap[20][146])
# print(distances[20][146])