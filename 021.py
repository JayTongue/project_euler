def sum_divisors(z):
    divisors = []
    for i in range(1, z):
        if not z % i:
            divisors.append(i)
    return sum(divisors)

lim, mem = 10001, set()
for j in range(2, lim):
    k = sum_divisors(j)
    if k!= j and k < lim and sum_divisors(k) == j:
        mem.add(j)
        mem.add(k)

print(sum(mem))

