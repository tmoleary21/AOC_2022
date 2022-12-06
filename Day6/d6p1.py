
with open("input.txt", "r") as f:
    buffer = f.read()

last_4 = buffer[:4]
bufferDistance = -1
for i in range(4,len(buffer)):
    if len(last_4) == len(set(last_4)):
        bufferDistance = i
        break
    last_4 = last_4[1:] + buffer[i]

print("The number of characters processed before start-of-message marker is", bufferDistance)