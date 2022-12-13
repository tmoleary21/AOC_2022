import ast

def compare(left, right):
    i = -1
    for i in range(len(left)):
        if i >= len(right):
            # Right finished first
            return -1
        if isinstance(left[i], int) and isinstance(right[i], int):
            if left[i] < right[i]:
                return 1 #Correct
            if left[i] > right[i]:
                return -1 #Incorrect
        elif isinstance(left[i], list) and isinstance(right[i], list):
            subresult = compare(left[i], right[i])
            if abs(subresult) == 1:
                return subresult
        else:
            # one of both types
            if isinstance(left[i], int):
                subresult = compare([left[i]], right[i])
                if abs(subresult) == 1:
                    return subresult
            else:
                subresult = compare(left[i], [right[i]])
                if abs(subresult) == 1:
                    return subresult
    if i < len(right)-1:
        # Right not done
        return 1
    return 0



with open('input.txt', 'r') as f:
    packet_pairs = f.read()[:-1].split('\n\n')


correct_indices = []
for i in range(len(packet_pairs)):
    pair = packet_pairs[i].split('\n')
    left = ast.literal_eval(pair[0])
    right = ast.literal_eval(pair[1])
    if compare(left, right) == 1:
        correct_indices.append(i+1)

print(sum(correct_indices))