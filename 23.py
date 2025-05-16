def div(n):
    return sum(i for i in range(1, n//2+1) if not n % i)

abundants = set(i for i in range(1, 28124) if div(i) > i)
total = 0
for j in range(1, 28124):
    if not any((j-a) in abundants for a in abundants if a <= j):
        total += j
print(total)