from tqdm import tqdm
from math import prod

def R(p):
    return prod([((i ** 3) - (i * 3) + 4) for i in range(0, p)]) % p

sol = 0

for i in tqdm(range(int(1e9), int(11e9))):
    sol += R(i)

print(sol)