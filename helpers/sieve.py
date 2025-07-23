from numba import jit

@jit
def bool_sieve(num):
    if num < 2:
        return [False] * (num + 1)
    
    prime = [True] * (num + 1)
    p = 2
    while p * p <= num:
        if prime[p]:
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1
    prime[0], prime[1] = False, False
    return prime
