from math import prod
from fractions import Fraction
from helpers.prime_factorization import prime_factorize
from tqdm import tqdm

def find_phi(search_space):
    prime_factors = set(prime_factorize(search_space))
    phi = search_space * prod([1 - Fraction(1, pf) for pf in prime_factors])
    if phi.denominator == 1:
        return phi.numerator
    else:
        return round(float(phi))
    
def main():
    ans_ratio, sol = 100000000, 0
    search_space = 1e7
    for i in tqdm(range(2, int(search_space))):
        phi = find_phi(i)
        if sorted(list(str(i))) == sorted(list(str(phi))):
            ratio = i/phi
            if ratio < ans_ratio:
                ans_ratio, sol = ratio, i
    print(sol)

    
if __name__ == '__main__':
    main()

# print(find_phi(9999889))