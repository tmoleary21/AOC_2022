
with open("input.txt", "r") as f:
    instructions = f.read().split('\n')[:-1]

x_reg = 1

total = 0
cycle = 1

def cycleActions():
    global x_reg, total, cycle
    if (cycle - 20) % 40 == 0:
        total += cycle * x_reg
    cycle += 1

for pc in range(len(instructions)):
    parts = instructions[pc].split(' ')
    if parts[0] == 'addx':
        cycleActions() #Cycle 1
        cycleActions() #Cycle 2
        x_reg += int(parts[1])
    else:
        cycleActions()

print(total)