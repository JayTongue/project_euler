from itertools import product
from tqdm import tqdm

def triangle(n):
    return n*(n+1)/2

def square(n):
    return n ** 2

def pentagonal(n):
    return n*(3 * n - 1)/2

def hexagonal(n):
    return n*(2 * n -1)

def heptagonal(n):
    return n*(5 * n - 3)/2

def octagonal(n):
    return n*(3 * n - 2)

tri_set, squa_set, pent_set, hexa_set, hept_set, octa_set = set(), set(), set(), set(), set(), set()
sets = tri_set, squa_set, pent_set, hexa_set, hept_set, octa_set
funcs = (triangle, square, pentagonal, hexagonal, heptagonal, octagonal)
for func, type_set in zip(funcs, sets):
    start = 1
    while True:
        generated = func(start)
        if generated <= int(1e4):
            if  generated >= 1000:
                type_set.add(generated)
        else:
            break
        start += 1


num_sets = [tri_set, squa_set, pent_set, hexa_set, hept_set, octa_set]
num_sets = [set(map(int, s)) for s in num_sets]
tri_set, squa_set, pent_set, hexa_set, hept_set, octa_set = num_sets

for combo in tqdm(product(tri_set, squa_set, pent_set, hexa_set, hept_set, octa_set)):
    tri_num, squa_num, pent_num, hexa_num, hept_num, octa_num = combo
    firsts, seconds = set([string[:2] for string in map(str, combo)]), set([string[2:] for string in map(str, combo)])
    if tuple(map(len, (firsts, seconds))) == (6, 6) and firsts == seconds and not any(str(string)[:2] == str(string)[2:] for string in combo):
        print(combo, sum(combo))
        break