import re

def trianglize(n):
    return 0.5* n * (n+1)

precompute = []
for i in range(1, 1000):
    precompute.append(trianglize(i))

lookup = {"A": 1,
            "B": 2,
            "C": 3,
            "D": 4,
            "E": 5,
            "F": 6,
            "G": 7,
            "H": 8,
            "I": 9,
            "J": 10,
            "K": 11,
            "L": 12,
            "M": 13,
            "N": 14,
            "O": 15,
            "P": 16,
            "Q": 17,
            "R": 18,
            "S": 19,
            "T": 20,
            "U": 21,
            "V": 22,
            "W": 23,
            "X": 24,
            "Y": 25,
            "Z": 26}
count = 0
with open('data/42.txt', 'r') as data:
    data = re.sub(r'\"', '', data.read()).split(',')
for word in data:
    total = 0
    word = list(word)
    for letter in word:
        total += lookup[letter]
    if total in precompute:
        count += 1

print(count)