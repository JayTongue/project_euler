def fib(seq):
    new = seq[-1] + seq[-2]
    if new > 4e6:
        return seq
    else:
        seq.append(new)
        return fib(seq)
print(sum(i for i in fib([1, 2]) if i % 2 == 0))


