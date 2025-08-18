from fractions import Fraction
from math import ceil, floor
from tqdm import tqdm

search_space = 12_000
sol_set = set()


for d in tqdm(range(1, search_space + 1)):
    start, stop = Fraction(d, 3), Fraction(d, 2)
    top, bottom = ceil(start), floor(stop)
    numers = [n for n in range(ceil(start), floor(stop)+1) 
              if Fraction(n, d) != Fraction(1, 2) and Fraction(n, d) != Fraction(1, 3)]
    fracs = [Fraction(n, d) for n in numers]
    if numers:
        sol_set.update(set(fracs))
print(len(sol_set))