from helpers.is_prime import is_prime
from helpers.timer import timer
from itertools import combinations
from tqdm import tqdm

@timer
def main():
    prime_array, prime_bools, small_primes = [], [], []
    good, bad = set(), set()

    for n in range(int(1e8)):
        if is_prime(n):
            prime_array.append(n)
            prime_bools.append(True)
            if n < 10000:
                small_primes.append(n)
        else:
            prime_bools.append(False)

    def check_swapy(good, bad, elements_tuple):
        for a, b in combinations(elements_tuple, 2):
            ab_set = frozenset((a, b))
            if ab_set in good:
                continue
            elif ab_set in bad:
                return False
            else:
                if all((prime_bools[int(f'{a}{b}')], prime_bools[int(f'{b}{a}')])):
                    good.add(ab_set)
                else:
                    bad.add(ab_set)
                    return False
        return True

    start_list = [tuple(pair) for pair in combinations(small_primes, 2) if check_swapy(good, bad, pair)]

    solution = []
    set_length = 5
    for _ in range(set_length - 2):
        new_list = []
        for starter in tqdm(start_list):
            for smol in small_primes:
                test_list = starter + (smol,)
                if check_swapy(good, bad, test_list):
                    new_list.append(test_list)
                    if len(test_list) == set_length:
                        solution = test_list
                        break
            if solution:
                break
        start_list = new_list
    print(solution, sum(solution))

main()