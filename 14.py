def collaz(n, count):
    if n == 1:
        return count+1
    else:
        count += 1
        if n % 2 == 0:
            return collaz(n//2, count)
        else:
            return collaz(3*n+1, count)
    
longest, answer, threshold = 0, 0, 1e6
for i in range(1, int(threshold)):
    count = collaz(i, 0)
    if count > longest:
        longest, answer = count, i
print(answer)