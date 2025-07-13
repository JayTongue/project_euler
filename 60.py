from itertools import permutations, combinations
from helpers.is_prime import is_prime
from tqdm import tqdm
import sys

def permute(good, bad, combo):
    prime_flag = True
    for pair in permutations(combo, 2):
        a, b = pair
        key = frozenset((a, b))
        if key in bad:
            prime_flag = False
            break
        elif key in good:
            continue
        else:
            ab = int(f"{a}{b}")
            ba = int(f"{b}{a}")
            if is_prime(ab) and is_prime(ba):
                good.add(key)
            else:
                bad.add(key)
                prime_flag = False
                break
    return good, bad, prime_flag


search_space = 10000
primes = [i for i in range(3, search_space+1) if is_prime(i)]
bad, good = set(), set()

solutions = set()

for combo in tqdm(combinations(primes, 4)):
    good, bad, prime_flag = permute(good, bad, combo)
    if prime_flag:
         solutions.add(combo)
         print(combo, sum(combo))
    
for solution in solutions:
    for prime in primes:
        new_tuple = [i for i in solution]
        new_tuple.append(prime)
        good, bad, prime_flag = permute(good, bad, new_tuple)
        if prime_flag:
            print('SOLUTION:', new_tuple, sum(new_tuple))
            sys.exit()
            
