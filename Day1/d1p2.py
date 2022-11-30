
topThreeCalories = [0,0,0]
currentCalories = 0

def compareAndPlace(topThreeCalories, currentCalories):
    smallest = min(topThreeCalories)
    smallestIndex = topThreeCalories.index(smallest)
    if currentCalories > smallest:
        topThreeCalories[smallestIndex] = currentCalories

with open("input.txt", "r") as inputFile:
    for line in inputFile:
        if len(line.strip()) == 0:
            compareAndPlace(topThreeCalories, currentCalories)
            currentCalories = 0
        else:
            currentCalories += int(line)
    compareAndPlace(topThreeCalories, currentCalories) #Ensure final elf is counted

    topThreeTotal = sum(topThreeCalories)
    print("The top 3 carriers are carrying", topThreeTotal, "total calories.")