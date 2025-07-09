from itertools import permutations
from tqdm import tqdm

def str_xor(s1, s2):
#  return s1 ^ s2
 return "".join([chr(ord(c1) ^ ord(c2)) for (c1,c2) in zip(s1,s2)])

with open('data/58.txt', 'r') as data:
   data = data.read().split(',')

for lowercase in tqdm(set(permutations(list('abcdefghijklmnopqrstuvwxyz')*3, 3))):
    lowercase_exp = lowercase*(len(data)//3)
    result = ''.join([str_xor(i, j) for i, j in zip(data, lowercase_exp)])
    if "to" in result.lower() and "^" not in result.lower() and "@" not in result:
       print(lowercase, result)
       print('-------------')