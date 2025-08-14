from math import prod
from tqdm import tqdm
from helpers.timer import timer
from helpers.prime_factorization import prime_factorize
from fractions import Fraction

@timer
def main():
    search_space = 1e6
    max_val, sol = 0, 0
    for i in tqdm(range(2, int(search_space))):
        phi = find_phi(i)
        div_val = i / phi
        if div_val > max_val:
            max_val, sol = div_val, i
    print(sol)

def find_phi(search_space):
    prime_factors = set(prime_factorize(search_space))
    phi = search_space * prod([1 - Fraction(1, pf) for pf in prime_factors])
    if phi.denominator == 1:
        return phi.numerator
    else:
        return round(float(phi))

if __name__ == '__main__':
    main()