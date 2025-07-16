from itertools import chain

def concat(num, limit):
    num_list = [num*(i+1) for i in range(limit)]
    digits = list(map(int, chain.from_iterable([list(str(n)) for n in num_list])))
    return digits
def pan(num, limit):
    digits = concat(num, limit)
    if len(digits) != 9:
        return False
    elif set(digits) == set([1, 2, 3, 4, 5, 6, 7, 8, 9]):
        return True
    else:
        return False

answer = 0
for limit in range(10):
    for num in range(int(2e6)):
        if pan(num, limit) and int(''.join(map(str, concat(num, limit)))) > answer:
            answer = int(''.join(map(str, concat(num, limit))))
print(answer)