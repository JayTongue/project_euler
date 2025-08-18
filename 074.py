from tqdm import tqdm

def factorialize(n, factorial=1):
    if n == 1 or n == 0:
        return factorial
    else:
        factorial *= n
        return factorialize(n-1, factorial)
    
tab = [factorialize(i) for i in range(10)]

def recombine(trial):
    trial = map(int, list(str(trial)))
    trial_sum = sum([tab[digit] for digit in trial])
    return trial_sum

def find_loop(trial, loop):
    if trial in loop:
        return loop
    else:
        loop.add(trial)
        recomb = recombine(trial)
        return find_loop(recomb, loop)
    
search_space = 1e6
sol = 0

for cand in tqdm(range(int(search_space))):
    loop = find_loop(cand, loop=set())
    if len(loop) == 60:
        sol += 1
print(sol)