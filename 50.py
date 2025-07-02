from helpers.is_prime import is_prime

primes = [i for i in range(2, int(1e6)) if is_prime(i)]

prefix = [0]
for p in primes:
    prefix.append(prefix[-1] + p)

answer = 0
max_len = 0

for start in range(len(primes)):
    for end in range(start + max_len + 1, len(primes) + 1):  # only check longer windows
        total = prefix[end] - prefix[start]
        if total >= int(1e6):
            break
        if is_prime(total):
            answer = total
            max_len = end - start

print(answer)
