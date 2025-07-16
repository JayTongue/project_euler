from itertools import permutations

def str_xor(s1, s2):
 return chr(ord(s1) ^ ord(s2))

with open('data/58.txt', 'r') as data:
   data = list(map(chr, map(int, data.read().split(','))))
   # print(data)

for lowercase in set(permutations(list('abcdefghijklmnopqrstuvwxyz')*3, 3)):
    lowercase_exp = lowercase*(len(data)//3)
    result = ''.join([str_xor(i, j) for i, j in zip(data, lowercase_exp)])
    if not any(char in result for char in ['*', '^', '@', '%', '$', '{']):
       print(lowercase, result)
       break
print(sum(map(ord, [i for i in list(result)])))