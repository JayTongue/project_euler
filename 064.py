from fractions import Fraction
from math import isqrt, sqrt
from decimal import Decimal, getcontext
from helpers.timer import timer
from tqdm import tqdm

getcontext().prec = 1000

def find_segments(loop):
    for i in range(0, len(loop)):
        chunk = loop[:i+1]
        repeated = chunk*(len(loop)//len(chunk))
        if repeated == loop[:len(repeated)]:
            return chunk
        
def continued_fraction_period(start):
    zero, one, a0 = 0, 1, isqrt(start)
    if a0 * a0 == start:
        return 0  # perfect square, no period

    a = a0
    period = 0
    seen = set()

    while True:
        zero = one * a - zero
        one = (start - zero * zero) // one
        a = (a0 + zero) // one
        period += 1
        if a == 2 * a0:
            return period
        
# def continued_fractions(start):
#     root = start.sqrt()
#     if sqrt(start) % 1 == 0:
#         return []
#     a0 = int(root)
#     a1 = Decimal(1) / (root - a0)
#     loops = [int(a1)]
#     for _ in range(150):
#         a2 = Decimal(1) / (a1 - int(a1))
#         loops.append(int(a2))
#         a1 = a2
#     chunk = find_segments(loops)
#     return chunk

@timer
def main():
    search_space = int(1e4)
    sol = 0

    for n in tqdm(range(2, search_space + 1)):
        if continued_fraction_period(n) % 2 == 1:
            sol += 1

    # for i in tqdm(range(2, search_space + 1)):
    #     chunk = continued_fractions(i)
    #     if chunk:
    #         if len(chunk) % 2 == 1:
    #             sol += 1
    print(sol)

main()
