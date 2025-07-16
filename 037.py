from helpers.is_prime import is_prime

def trim(num):
    num = [int(n) for n in list(str(num))]
    forward = [num[:it] for it in range(len(num)+1)if num[:it]]
    backward = [num[it:] for it in range(len(num)+1) if num[it:] and num[it:] not in forward]
    iterations = forward + backward
    iterations = [int(''.join(map(str, iteration))) for iteration in iterations]
    if all(map(is_prime, iterations)):
        return True
    else:
        return False

total = 0
for i in range(int(1e6)):
    if i not in (2, 3, 5, 7) and trim(i):
        total += i
print(total)