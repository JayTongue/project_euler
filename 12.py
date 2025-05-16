def divis(n):
    count, i = 1, 2
    while i <= n ** (1/2):
        power = 0
        while n % i == 0:
            n //= i
            power += 1
        count *= (power + 1)
        i += 1
    if n > 1:
        count *= 2
    return count

count, tri_start, tri_add = 0, 0, 1
while count < 500:
    tri_start += tri_add
    count = divis(tri_start)
    # print(count, tri_start)
    tri_add += 1
print(tri_start)