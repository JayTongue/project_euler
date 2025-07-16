import numpy as np
from helpers.is_prime import is_prime

seed = np.array([[5, 4, 3], [6, 1, 2], [7, 8, 9]])
# print(seed, seed.shape)

def add_side(seed):
    seed = np.rot90(seed, 3)
    add_bottom = np.array([i for i in range(seed.max()+1, seed.max()+seed.shape[1]+1)])
    # print(seed.shape, add_bottom) 
    seed = np.append(seed, [add_bottom], axis=0)
    return seed

def wrap(seed):
    # for wrap_count in range(wraps):
    for _ in range(4):
        seed = add_side(seed)
        # print(seed, seed.shape)

    diags =  set(map(int, [seed[i, i] for i in range(0, seed.shape[0])] + [seed[i, seed.shape[1]-i-1] for i in range(0, seed.shape[0])]))
    prime_count = list(map(is_prime, diags)).count(True)
    return prime_count/len(diags)*100, seed

prime_percent = 100
while prime_percent > 10:
    prime_percent, seed = wrap(seed)
    if (seed.shape[0]-1) % 100 == 0:
        print(seed.shape[0], prime_percent)
print(prime_percent, seed.shape)
