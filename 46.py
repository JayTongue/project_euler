from helpers.is_prime import is_prime

for n in range(9, int(1e8)):
    solveable = False
    if is_prime(n):
        continue
    for power in range(1, 100):
        if is_prime(n-(2*(power**2))):
            solveable = True
    if not solveable and n % 2 == 1:
        print(n)
        break