def count_sols(perimeter):
    answer = set()
    for a in range(1, perimeter):
        for b in range(1, perimeter - a):
            c = perimeter - a - b
            if a**2 + b**2 == c**2:
                answer.add(frozenset((a, b, c)))
    return len(answer)

solutions, answer = 0, 0
for perimeter in range(1000):
    count = count_sols(perimeter)
    if count > solutions:
        answer, solutions = perimeter, count
print(solutions, answer) 