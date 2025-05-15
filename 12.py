divisor_count, adder, triangle_sum = 1, 1, 0
while divisor_count <= 500:
    divisor_count = 2
    for i in range(2, triangle_sum//2 + 1):
        if triangle_sum % i == 0:
            divisor_count += 1
    triangle_sum += adder
    adder += 1
print(triangle_sum - adder + 1)