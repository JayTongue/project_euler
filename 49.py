from helpers.is_prime import is_prime

for i in range(1000, 10000):
    j, k = i + 3330, i + 6660
    length = len(set([frozenset(list(str(i))), frozenset(list(str(j))), frozenset(list(str(k)))]))
    if length == 1 and all(map(is_prime, [i, j, k])):
        print(''.join(map(str, [i, j, k]))) 
