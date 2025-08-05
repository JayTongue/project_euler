'''
given 

      3
     7 4
    2 4 6
   8 5 9 3


Start at row: [8, 5, 9, 3]
Then row above: [2, 4, 6] becomes:

[2 + max(8,5) = 10,
 4 + max(5,9) = 13,
 6 + max(9,3) = 15] → [10, 13, 15]

Then: [7,4] → [7 + max(10,13) = 20, 4 + max(13,15) = 19] → [20,19]

Finally: [3 + max(20,19) = 23]

'''

with open('data/67.txt', 'r') as data:
    data = data.readlines()[:-2]
    data = [list(map(int, line.split(' '))) for line in data]

for count, number in enumerate(data[-2]):
    