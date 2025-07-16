def trial(target):
    primes, start = [2], 3
    while len(primes) < target:
        flag = True
        for prime in primes:
            if start % prime == 0:
                flag = False
                break
        if flag:
            primes.append(start)
        start += 1
    return primes[-1]

target = 10001
print(trial(target))