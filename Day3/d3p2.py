
itemtypes = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

file = ""

with open("input.txt", "r") as f:
    file = f.read()

rucksacks = file.split("\n")[:-1]

def getBadgePriority(rucksacks, start):
    ruck1 = rucksacks[start]
    ruck2 = rucksacks[start+1]
    ruck3 = rucksacks[start+2]
    for item in ruck1:
        if item in ruck2 and item in ruck3:
            return itemtypes.index(item)+1
    return 0


priority_sum = sum([getBadgePriority(rucksacks, i) for i in range(0, len(rucksacks), 3)])
print("Sum of priorities is", priority_sum)