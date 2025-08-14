from fractions import Fraction
from tqdm import tqdm
from math import gcd

search_space = 1e6
target = Fraction(3, 7)
sol = Fraction(0, 1)

for d in range(1, int(search_space) + 1):
    n = (3 * d - 1) // 7
    if gcd(n, d) == 1:
        f = Fraction(n, d)
        if f > sol:
            sol = f
print(sol)