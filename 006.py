choice = 100
each = sum([i**2 for i in range(1, choice + 1)])
single = sum(range(1, choice + 1))**2
print(single - each)