max_range = 100
all_set = set()
for a in range(2, max_range+1):
    for b in range(2, max_range+1):
        all_set.add(a**b)
print(len(all_set))