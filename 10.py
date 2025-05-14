primes = [2]
for i in range(3, int(2e6)):
    flag = True
    for prime in primes:
        if i % prime == 0:
            flag = False
    if flag:
        primes.append(i)
print(sum(primes))