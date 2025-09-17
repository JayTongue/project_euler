from helpers.sieve import bool_sieve

search_space = int(1e2)
bool_sieve = bool_sieve(search_space)

total_sum = 10
for count, b in enumerate(bool_sieve):
    if b:
        # print(count)
        combos = []
        sum_bool = bool_sieve[:total_sum]
        print(sum_bool)
        
        