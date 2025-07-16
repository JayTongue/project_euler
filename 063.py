search_space = 100
sol = 0
for power in range(1, search_space):
    powers = [i**power for i in range(1, search_space) if len(list(str(i**power))) == power]
    if powers:
        print(powers, len(powers))
    sol += len(powers)
print(sol)