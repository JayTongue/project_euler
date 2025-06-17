from helpers.is_prime import is_prime
from tqdm import tqdm
from functools import cache

# @cache
# def main():
#     primes = [i for i in range(2, int(1e6)) if is_prime(i)]
#     answer, answer_list = 0, []
#     for wind in tqdm(range(2, len(primes))):
#         for j in range(len(answer_list)+1, len(primes)):
#             try:
#                 trial_list = [primes[j+k] for k in range(wind)]
#                 if is_prime(sum(trial_list)) and wind > len(answer_list) and sum(trial_list) < int(1e6):
#                     answer, answer_list = sum(trial_list), trial_list
#             except IndexError:
#                 continue
#     print(answer, answer_list)


primes = [i for i in range(2, int(1e6)) if is_prime(i)]

# Build prefix sums
prefix = [0]
for p in primes:
    prefix.append(prefix[-1] + p)

answer = 0
max_len = 0

# Try all windows (start, end)
for start in range(len(primes)):
    for end in range(start + max_len + 1, len(primes) + 1):  # only check longer windows
        total = prefix[end] - prefix[start]
        if total >= int(1e6):
            break
        if is_prime(total):
            answer = total
            max_len = end - start

print(answer)
