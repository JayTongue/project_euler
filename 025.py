import sys
sys.setrecursionlimit(10 ** 6) # now THIS is podracing
def fib(n, seq):
    if len(list(str(seq[-1]))) == n:
        return len(seq)
    else:
        seq.append(seq[-1] + seq[-2])
        return fib(n, seq)
    

print(fib(1000, [1, 1]))