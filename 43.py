from itertools import permutations
from tqdm import tqdm
# perm = [int(''.join(str(g) for g in p)) for p in permutations(list(range(10)))]
perm = [list(tup) for tup in permutations(list(range(10)))]

def find_property(digit_list):
    divis = (2, 3, 5, 7, 11, 13, 17)
    start, end = (1, 4)
    works = True
    for prime in divis:
        digit_int = int(''.join(str(n) for n in digit_list[start:end]))
        # print(prime, digit_int)
        if digit_int % prime == 0:
            start, end = start + 1, end + 1
        else:
            works = False
            break
    return works

final_sum = 0
for digit_list in tqdm(perm):
    if find_property(digit_list):
        final_sum += int(''.join(str(d) for d in digit_list))
print(final_sum)


# print(find_property([int(n) for n in str(1406357289)]))