import copy

def rotate(num):
    num = [int(i) for i in list(str(num))]
    rotations = [int(''.join(map(str,copy.deepcopy(num))))]
    for _ in range(len(num) -1):
        shifting = num.pop(0)
        num.append(shifting)
        rotations.append(int(''.join(map(str,copy.deepcopy(num)))))
    return rotations

def is_prime(n):
    if n <= 1:
        return False
    if n in [2, 3]: 
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False    
    for i in range(5, int(n **(1/2))+ 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

count = 0
for i in range(int(1e6)):
    if all(map(is_prime, rotate(i))):
        count+=1
print(count)