
itemtypes = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def getCommonItemPriority(rucksack):
    halfindex = int(len(rucksack)/2)
    comp1 = rucksack[:halfindex]
    comp2 = rucksack[halfindex:]
    for item in comp1:
        if item in comp2:
            return itemtypes.index(item)+1
    return 0

priority_sum = sum([getCommonItemPriority(rucksack) for rucksack in open("input.txt", "r")])
print("Sum of priorities is", priority_sum)