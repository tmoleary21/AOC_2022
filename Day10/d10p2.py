
with open("input.txt", "r") as f:
    instructions = f.read().split('\n')[:-1]

x_reg = 1
cycle = 1
outString = ''

def cycleActions():
    global x_reg, cycle, outString
    if (cycle-1) % 40 in [x_reg-1, x_reg, x_reg+1]:
        outString += '#'
    else:
        outString += '.'
    if cycle % 40 == 0:
        outString += '\n'
    cycle += 1

for pc in range(len(instructions)):
    parts = instructions[pc].split(' ')
    print(cycle, instructions[pc])
    if parts[0] == 'addx':
        cycleActions() #Cycle 1
        cycleActions() #Cycle 2
        x_reg += int(parts[1])
    else:
        cycleActions()

print(outString)