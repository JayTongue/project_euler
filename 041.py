from helpers.is_prime import is_prime

answer = 0
for i in range(2, 987654321):
    if (set(map(int, list(str(i)))) == set([j for j in range(1, len(list(str(i)))+1)])) and is_prime(i) and i > answer:
        answer = i
print(answer)       