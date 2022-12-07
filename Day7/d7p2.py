
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

def findDirToDelete(root, spaceNeeded):
    root_size = calcSingleTotal(root)
    closest = root_size if root_size >= spaceNeeded else 70_000_000
    for (k,v) in root.items():
        if isinstance(v, dict) and k != '..':
            dir_closest = findDirToDelete(v, spaceNeeded)
            if dir_closest < closest and dir_closest >= spaceNeeded:
                closest = dir_closest
    return closest



with open("input.txt", "r") as f:
    terminal = f.read()

root = {}
formDirectoryStructure(root, terminal)

spaceNeeded = 30_000_000 - (70_000_000 - calcSingleTotal(root))

print(findDirToDelete(root, spaceNeeded))
