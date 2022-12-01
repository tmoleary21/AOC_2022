
roundValues = {
    'A Y' : 4,
    'B Z' : 9,
    'C X' : 2,
    'A Z' : 8,
    'B X' : 1,
    'C Y' : 6,
    'A X' : 3,
    'B Y' : 5,
    'C Z' : 7,
    '' : 0
}

strategy = ""

with open("input.txt", "r") as file:
    strategy = file.read()

score = sum([roundValues[round] for round in strategy.split('\n')])
print("Strategy score is", score)