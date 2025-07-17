from math import sqrt

def find_segments(loop):
    for i in range(0, len(loop)):
        chunk = loop[:i+1]
        repeated = chunk*(len(loop)//len(chunk))
        if repeated == loop[:len(repeated)]:
            return chunk
        

def continued_fractions(start):
    if sqrt(start) % 1 == 0:
        return []
    a0 = int(sqrt(start) // 1)
    a1 = 1/(sqrt(start) - a0)
    loops = [int(a1)]
    for _ in range(18):
        a2 = 1 / (a1 - int(a1))
        loops.append(int(a2))
        a1 = a2
    chunk = find_segments(loops)
    return chunk

search_space = 13
for i in range(2, search_space + 1):
    chunk = continued_fractions(i)
    print(chunk)
    