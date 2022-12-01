
roundValues = {
    'A Y' : 8,
    'B Z' : 9,
    'C X' : 7,
    'A Z' : 3,
    'B X' : 1,
    'C Y' : 2,
    'A X' : 4,
    'B Y' : 5,
    'C Z' : 6,
    '' : 0
}

strategy = ""

with open("input.txt", "r") as file:
    strategy = file.read()

score = sum([roundValues[round] for round in strategy.split('\n')])
print("Strategy score is", score)