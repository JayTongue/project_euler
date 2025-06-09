from fractions import Fraction
from math import prod
def compare(a_start, a_end, b_start, b_end):
    try:
        if a_start in (b_start, b_end):
            denom = [b_start, b_end]
            denom.remove(a_start)
            if a/b == a_end/denom[0]:
                if a != b and a_start != 0:
                    return (a, b)
    except ZeroDivisionError:
        return None
fracs = []
for a in range(10, 100):
    a_start, a_end = int(list(str(a))[0]), int(list(str(a))[1])
    for b in range(10, 100):
        b_start, b_end = int(list(str(b))[0]), int(list(str(b))[1])
        if a/b > 1:
            continue
        fracs.append(compare(a_start, a_end, b_start, b_end))
        fracs.append(compare(a_end, a_start, b_start, b_end))
fracs = list(filter(lambda x: x is not None, fracs))
numers, denoms = prod([n for n, d in fracs]), prod([d for n, d in fracs])
print(Fraction(numers, denoms))


