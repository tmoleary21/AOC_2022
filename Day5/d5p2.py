
stacks = [] # Each element is a stack of crates (list of crate letters)

def buildStacks(stacks, input):
    stackIndex = 0
    for strIndex in range(1, len(input[-1]), 4):
        stacks.append([])
        for height in range(len(input)-2, -1, -1):
            crate = input[height][strIndex]
            if crate != ' ':
                stacks[stackIndex].append(crate)
        stackIndex += 1

# Helpful for debugging
def printPrettyStacks(stacks):
    print('-----------------------')
    for i in range(len(stacks)):
        stackStr = ''
        for crate in stacks[i]:
            stackStr += crate
        print(i, stackStr)
    print('-----------------------')

def performInstructions(stacks, instructions):
    for instruction in instructions:
        instructionParts = instruction.split(' ')
        numToMove = int(instructionParts[1])
        fromIndex = int(instructionParts[3])-1
        toIndex = int(instructionParts[5])-1
        # printPrettyStacks(stacks)
        stacks[toIndex].extend(stacks[fromIndex][-numToMove:])
        stacks[fromIndex] = stacks[fromIndex][:-numToMove]

def concatTops(stacks):
    result = ''
    for stack in stacks:
        result += stack[-1]
    return result


with open("input.txt", "r") as f:
    parts = f.read().split('\n\n')
    instructions = parts[1].split('\n')[:-1]
    buildStacks(stacks, parts[0].split('\n'))

performInstructions(stacks, instructions)
print('The top of each stack is:\n' + concatTops(stacks))
