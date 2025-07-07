def sum_digits(n):
    return sum(map(int, list(str(n))))

answer = 0
for a in range(1, 101):
    for b in range(1, 101):
        digit_sum = sum_digits(a**b)
        if digit_sum > answer:
            answer = digit_sum
print(answer)
