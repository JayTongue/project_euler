from collections import defaultdict
from helpers.timer import timer

def make_triples(m, n):
    if n != m and all(map(lambda x: isinstance(x, int), (m, n))):
        a, b, c = (m**2 - n**2), (2*m*n), (m**2 + n**2)
        return set(map(abs, {a, b, c}))
    else:
        raise ValueError('m and n have to be different ints!')

@timer
def main():
    search_space = int(15e5)
    big_dict = defaultdict(set)
    start = 1

    while start < search_space:
        sum_progress = 0
        n = start + 1
        while sum_progress < search_space:
            a, b, c = make_triples(start, n)
            sum_progress = sum((a, b, c))
            
            if sum_progress > search_space:
                break
            else:
                big_dict[sum_progress].add(frozenset({a, b, c}))
                multiplier = 2

                d, e, f = a, b, c
                while sum((d, e, f)) < search_space:
                    d, e, f = [side*multiplier for side in (a, b, c)]
                    big_dict[sum((d, e, f))].add(frozenset({d, e, f}))
                    multiplier += 1
                n += 1
        start += 1

    sol = 0
    for k, v in big_dict.items():
        if len(v) == 1 and k < search_space:
            sol += 1
    print(sol)

main()