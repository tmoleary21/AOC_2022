
def findIndividualScore(rows, x, y):
    score = 1
    sideLength = len(rows)
    for i in range(1,sideLength):
        if x+i == sideLength-1 or rows[y][x+i] >= rows[y][x]:
            score *= i
            break
    for i in range(1,sideLength):
        if x-i == 0 or rows[y][x-i] >= rows[y][x]:
            score *= i
            break
    for i in range(1,sideLength):
        if y+i == sideLength-1 or rows[y+i][x] >= rows[y][x]:
            score *= i
            break
    for i in range(1,sideLength):
        if y-i == 0 or rows[y-i][x] >= rows[y][x]:
            score *= i
            break
    return score

with open("input.txt", "r") as f:
    grid = f.read()

rows = grid.split('\n')[:-1]
sideLength = len(rows)

maxScore = 0
for i in range(1, sideLength-1):
    for j in range(1, sideLength-1):
        score = findIndividualScore(rows, j, i)
        if score > maxScore:
            maxScore = score

print(maxScore)
        