def quad(x, a, b):
    return x**2 + a*x + b

def is_prime(n):
    if n <= 1:
        return False
    if n in [2, 3]: 
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False    
    for i in range(5, int(n **(1/2))+ 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

answer, product = 0, 0
for a in range(-1000, 1000):
    for b in range(-1001, 1001):
        prime, x, count = True, 0, 0
        while prime:
            prime = is_prime(quad(x, a, b))
            x += 1
            count += 1
        if count > answer:
            answer, product = count, a * b

print(product)