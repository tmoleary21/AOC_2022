import ast
from functools import cmp_to_key

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
    unparsed_packets = f.read()[:-1].replace('\n\n', '\n').split('\n')

packets = [ast.literal_eval(packet) for packet in unparsed_packets]
packets.extend([[[2]], [[6]]])

sorted_packets = sorted(packets, key=cmp_to_key(compare), reverse=True)

decoder_key = (sorted_packets.index([[2]])+1) * (sorted_packets.index([[6]])+1)
print(decoder_key)
