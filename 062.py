from collections import defaultdict
from helpers.timer import timer

@timer
def find(n):
    cubes = defaultdict(list)
    i = 1
    while True:
        cube = i ** 3
        key = ''.join(sorted(str(cube)))
        cubes[key].append(cube)
        if len(cubes[key]) == n:
            return min(cubes[key])
        i += 1
print(find(5))