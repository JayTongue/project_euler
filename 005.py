def gcd(i, j):
    while j: # euler's to recursively solve until 0
        i, j, = j, i % j
    return i
def lcm(i, j):
    return (i * j)/gcd(i, j)

result = 1
for k in range(1, 21):
    result = lcm(result, k)
print(result)