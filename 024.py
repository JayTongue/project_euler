from itertools import permutations

for count, perm in enumerate(permutations(list(range(10)))):
    if count == (1e6 - 1):
        print(int(''.join([str(digit)for digit in perm])))