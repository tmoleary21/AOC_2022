
def findNUnique(n, buffer):
    last_n = buffer[:n]
    bufferDistance = -1
    for i in range(n,len(buffer)):
        print(last_n)
        if len(last_n) == len(set(last_n)):
            bufferDistance = i
            break
        last_n = last_n[1:] + buffer[i]
    return bufferDistance


with open("input.txt", "r") as f:
    buffer = f.read()

print("The number of characters processed before start-of-packet marker is", findNUnique(14, buffer))