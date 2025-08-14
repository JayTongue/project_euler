from fractions import Fraction
from tqdm import tqdm
from helpers.prime_factorization import prime_factorize
from math import prod


def compute_totients(search_space):
    phi = list(range(search_space + 1))
    for i in range(2, search_space + 1):
        if phi[i] == i:
            for j in range(i, search_space + 1, i):
                phi[j] -= phi[j] //i
    return phi

def main():
    search_space = 1e6
    phi = compute_totients(int(search_space))
    print(sum(phi[2:]))

if __name__ == '__main__':
    main()


