can, factors, possible = 600851475143, [], True
while can > 1:
    for i in range(2, int(can**(1/2))):
        if can % i == 0:
            factors.append(i)
            can = can/i
print(max(factors))