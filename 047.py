
def prime_factorization(n, factors=None):
    if factors is None:
        factors = []
    for divisor in range(2, n+1):
        if n%divisor == 0:
            factors.append(divisor)
            return prime_factorization(n//divisor, factors)
    return set(factors)

test=10
while True:
    if [len(i) for i in map(prime_factorization, [test, test+1, test+2, test+3])] == [4, 4, 4, 4]:
        break
    test += 1
print(test)