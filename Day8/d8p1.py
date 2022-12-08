
with open("input.txt", "r") as f:
    grid = f.read()

rows = grid.split('\n')[:-1]
sideLength = len(rows)

visible = [[0] * sideLength for i in range(sideLength)]

for i in range(sideLength):
    leftMax = rightMax = topMax = bottomMax = -1
    for j in range(sideLength):
        #Left to Right
        value = int(rows[i][j])
        if value > leftMax:
            leftMax = value
            visible[i][j] = 1
        #Right to Left
        value = int(rows[i][(sideLength-1)-j])
        if value > rightMax:
            rightMax = value
            visible[i][(sideLength-1)-j] = 1
        #Top to Bottom
        value = int(rows[j][i])
        if value > topMax:
            topMax = value
            visible[j][i] = 1
        #Bottom to Top
        value = int(rows[(sideLength-1)-j][i])
        if value > bottomMax:
            bottomMax = value
            visible[(sideLength-1)-j][i] = 1

totalVisible = sum([sum(x) for x in visible])

print(totalVisible)
        