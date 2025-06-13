def pentagon(n):
    return int((n*((3*n)-1))/2)

precompute = set(pentagon(n) for n in range(1, 10000))

for i in range(1, 10000):
    for j in range(1, 10000):
        if (pentagon(i) + pentagon(j) in precompute) and (abs(pentagon(i) - pentagon(j)) in precompute):
            print(i, j, abs(pentagon(i) - pentagon(j)))