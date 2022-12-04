
with open("input.txt", "r") as f:
    content = f.read()

pairs = content.split()
elf_pairs = [pair.split(",") for pair in pairs]
print(elf_pairs)

def oneContainsOther(elf_pair):
    print(elf_pair)

    elfSet1 = elf_pair[0] #elf_pair[0,elf_pair.index('-')]
    elfSet2 = elf_pair[1] # elf_pair.index('-')+1,]

    print(elfSet1)
    print(elfSet2)

    print(elfSet1, elfSet2)
    elfSet1_split = elfSet1.split('-')
    elfSet2_split = elfSet2.split('-')
    if (int(elfSet2_split[0]) <= int(elfSet1_split[0]) and int(elfSet2_split[1]) >= int(elfSet1_split[1])):
        print(1)
        return 1
    elif((int(elfSet1_split[0]) <= int(elfSet2_split[0]) and int(elfSet1_split[1]) >= int(elfSet2_split[1]))):
        print(1)
        return 1
    else:
        print(0)
        return 0


# for elf_pair in elf_pairs:
#     print('-' in elf_pair)

count = sum([oneContainsOther(elf_pair) for elf_pair in elf_pairs if len(elf_pair) > 0])
print("Count of pairs that contain the other is", count)