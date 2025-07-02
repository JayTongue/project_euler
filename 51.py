from itertools import combinations
from helpers.is_prime import is_prime

def find_threshold(threshold):
    digits = 2
    highest, highest_row = 0, []
    while True:
        positions = []
        for j in range(1, digits+1):
            positions += combinations([i for i in range(digits)], j)
        # print(positions)

        for k in range(int(10**(digits-1)), int(10**digits)):
            original_k = list(str(k))
            for combination in positions:
                count, row = 0, set()
                for replacement in range(10):
                    k_copy = original_k.copy()
                    for digit in combination:
                        k_copy[digit] = str(replacement)  # make sure it's a string
                    if k_copy[0] != '0':  # leading zero check
                        k_int = int(''.join(k_copy))
                        if is_prime(k_int):
                            count += 1
                            row.add(k_int)

                if count == threshold:
                    return count, row
                if count > highest:
                    highest, highest_row = count, row
        print(f'digits: {digits}, highest: {highest, highest_row}')
        digits += 1
print(find_threshold(8))
    