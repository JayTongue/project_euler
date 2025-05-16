import re
with open('data/22.txt', 'r') as data:
    data = data.read()
data = [i.lower() for i in re.sub(r'\"', '', data).split(',')]
data.sort()
total = 0
for count, name in enumerate(data):
    name_total = 0
    for letter in name:
        name_total += ord(letter) - 96
    total += (count + 1) * name_total
print(total)