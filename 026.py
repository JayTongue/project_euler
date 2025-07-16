def recurring(numer, denom):
    remainders = {}
    remainder = numer % denom
    position = 0

    while remainder and remainder not in remainders:
        remainders[remainder] = position
        remainder = (remainder * 10) % denom
        position += 1
    if remainder == 0:
        return 0
    else:
        return position - remainders[remainder]

maxi, answer  = 0, 0
for i in range(1, 1000):
    if recurring(1, i) > maxi:
        maxi = i
print(maxi)