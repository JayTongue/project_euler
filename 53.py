def non_recursive_factorial(num):
    total = 1
    while num > 1:
        total *= num
        num -= 1
    return total

def combi(n, r):
    return int(non_recursive_factorial(n)/(non_recursive_factorial(r) * non_recursive_factorial(n - r)))

count = 0
for n in range(1, 101):
    for r in range(1, n+1):
        if combi(n, r) > int(1e6):
            count += 1
print(count)