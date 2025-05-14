ans = 0
def pal(prod):
    return str(prod) == str(prod)[::-1]
for i in range(100,1000):
    for j in range(100, 1000):
        prod = i * j
        if pal(prod) and prod > ans:
            ans = prod

print(ans)