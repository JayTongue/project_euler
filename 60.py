from helpers.timer import timer
from helpers.sieve import bool_sieve
from itertools import combinations
from tqdm import tqdm
import math

@timer
def main():
    good, bad = set(), set()

    search_space = int(1e8)
    bool_array = bool_sieve(search_space)
    small_primes = [count for count, n in enumerate(bool_array) if n and count < 10000]

    def check_swapy(good, bad, elements_tuple):
        def magnify(n):
            return 10 ** math.ceil(math.log10(n))
        for a, b in combinations(elements_tuple, 2):
            ab_set = frozenset((a, b))
            if ab_set in good:
                continue
            elif ab_set in bad:
                return False
            else:
                # if all((bool_array[int(f'{a}{b}')], bool_array[int(f'{b}{a}')])):
                if all((bool_array[(a * magnify(b)) + b], bool_array[(b * magnify(a)) + a])):
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