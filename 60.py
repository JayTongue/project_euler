from itertools import permutations, combinations
from helpers.is_prime import is_prime
from tqdm import tqdm

search_space = 3000
primes = [i for i in range(3, search_space+1) if is_prime(i)]

bad = set()

for combo in tqdm(combinations(primes, 5)):
    prime_flag = True
    for pair in permutations(combo, 2):
        if frozenset(pair) in bad:
            prime_flag = False
            break
        elif not is_prime(int(''.join(map(str, pair)))):
            bad.add(frozenset(pair))
            prime_flag = False
            break
    if prime_flag:
         print(combo, sum(combo))
         break
            
