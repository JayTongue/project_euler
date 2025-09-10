from helpers.timer import timer

def find_ways(breakdown, i, n, sol):
    if n == 0:
        sol += 1
        # print(breakdown)
    else:
        for j in range(i, n+1):
            breakdown.append(j)
            sol = find_ways(breakdown, j, n-j, sol)
            del breakdown[-1]
    return sol

@timer
def main():
    n = 100
    breakdown, sol = [], 0
    sol = find_ways(breakdown, 1, n, sol)
    print(sol-1)

main()
