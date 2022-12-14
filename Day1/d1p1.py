
maxCalories = 0
currentCalories = 0

with open("input.txt", "r") as inputFile:
    for line in inputFile:
        if len(line.strip()) == 0:
            if currentCalories > maxCalories:
                maxCalories = currentCalories
            currentCalories = 0
        else:
            currentCalories += int(line)
        if currentCalories > maxCalories: #Ensure final elf is counted
                maxCalories = currentCalories

    print("The elf carrying the most calories has", maxCalories, "calories.")