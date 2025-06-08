def factorial(x, total=1):
    if x in (0, 1):
        return total
    else:
        total *= x
        x -= 1
        return factorial(x, total)
    
def process(x, pre_process):
    x_list = [int(n) for n in list(str(x))]
    return x == sum([pre_process[n] for n in x_list])

pre_process = {}
for i in range(0, 10):
    pre_process[i] = factorial(i)

answer = 0
for i in range(10, 2540160):
    if process(i, pre_process):
        answer += i
print(answer)
