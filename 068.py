from itertools import permutations
from helpers.timer import timer

@timer
def main():
    size, length = 10, 16
    solutions = set()
    for perm in permutations([i for i in range(1, size+1)], size):
        shared = perm[:int(len(perm)/2)]
        added = perm[int(len(perm)/2):]
        smallest_idx = added.index(min(added))
        order = [smallest_idx + k for k in range(0, len(added)-smallest_idx)] + [j for j in range(0, smallest_idx)]
        triplet_indexes = [[x, x, (x+1)%len(added)] for x in range(len(added))]
        triplets = [[added[a], shared[b], shared[c]] for a, b, c in triplet_indexes]
        angles = map(sum, triplets)

        if len(set(angles)) == 1:
            chains = [''.join(map(str, (triplet))) for triplet in triplets]
            solution = ''.join([chains[idx] for idx in order])
            solutions.add(solution)
    sols = [solution for solution in solutions if len(solution) == length]
    print(max(map(int, sols)))

main()