class Monkey:
    def __init__(self, text_monkey):
        monkey_parts = text_monkey.split('\n')
        self.items = list(map(int, monkey_parts[1][monkey_parts[1].index(':')+2:].split(', ')))
        self.leftOperand, self.operator, self.rightOperand = monkey_parts[2].split(' ')[-3:]
        self.test_divisor = int(monkey_parts[3].split(' ')[-1])
        self.trueThrow = int(monkey_parts[4].split(' ')[-1])
        self.falseThrow = int(monkey_parts[5].split(' ')[-1])
        self.totalInspections = 0
    def __repr__(self) -> str:
        return f'{self.items} {self.operation} {self.test_divisor} {self.trueThrow} {self.falseThrow}'
    def inspect(self, old):
        self.totalInspections += 1
        if self.operator == '+':
            if self.leftOperand == 'old' and self.rightOperand == 'old':
                return old + old
            elif self.rightOperand == 'old':
                return int(self.leftOperand) + old
            else:
                return old + int(self.rightOperand)
        else:
            if self.leftOperand == 'old' and self.rightOperand == 'old':
                return old * old
            elif self.rightOperand == 'old':
                return int(self.leftOperand) * old
            else:
                return old * int(self.rightOperand)

        
def monkeyTurn(monkeys, index, modulus):
    monkey = monkeys[index]
    for i in range(len(monkey.items)):
        item = monkey.items[i]
        item = monkey.inspect(item) #Inspect
        # item //= 3 #Relief
        item %= modulus
        # Throw
        if item % monkey.test_divisor == 0:
            monkeys[monkey.trueThrow].items.append(item)
        else:
            monkeys[monkey.falseThrow].items.append(item)
    monkey.items = []



with open("input.txt", "r") as f:
    text_monkeys = f.read()[:-1].split('\n\n')

monkeys = []
modulus = 1
for text_monkey in text_monkeys:
    monkey = Monkey(text_monkey)
    modulus *= monkey.test_divisor
    monkeys.append(monkey)

for round in range(10000):
    for i in range(len(monkeys)):
        monkeyTurn(monkeys, i, modulus)

ranked_monkeys = sorted(monkeys, key= lambda x: x.totalInspections)
monkey_business = ranked_monkeys[-1].totalInspections * ranked_monkeys[-2].totalInspections
print(monkey_business)
