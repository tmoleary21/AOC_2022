
def formDirectoryStructure(root, terminal):
    workingDir = root
    for line in terminal.split('\n')[:-1]:
        parts = line.split(' ')
        if parts[0] == '$':
            #Command
            if parts[1] == 'cd':
                if parts[2] == '/':
                    workingDir = root
                else:
                    if parts[2] not in workingDir:
                        workingDir[parts[2]] = {'..':workingDir}
                    workingDir = workingDir[parts[2]]                
            if parts[1] == 'ls':
                pass
        else:
            # ls results
            if parts[0] == 'dir' and parts[1] not in workingDir:
                workingDir[parts[1]] = {'..':workingDir}
            else:
                workingDir[parts[1]] = parts[0]

def calcSingleTotal(root):
    total = 0
    for (k,v) in root.items():
        if not isinstance(v, dict):
            total += int(v)
        elif k != '..':
            total += calcSingleTotal(v)
    return total

def calcAllTotals(root):
    root_total = calcSingleTotal(root)
    total = root_total if root_total <= 100000 else 0 
    for (k,v) in root.items():
        if isinstance(v, dict) and k != '..':
            total += calcAllTotals(v)
    return total



with open("input.txt", "r") as f:
    terminal = f.read()

root = {}
formDirectoryStructure(root, terminal)

print(calcAllTotals(root))
