def factorial(n, total):
    total *= n
    if n == 1:
        return total
    else:
        return factorial(n-1, total)
    
print(sum([int(i) for i in list(str(factorial(100, 1)))]))