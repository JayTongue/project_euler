from tqdm import tqdm
def test(x):
    if x == sum([int(i)**5 for i in str(x)]):
        return True
    else:
        return False
total, count = 0, 0
for i in tqdm(range(2, int(1e6))):
    if test(i):
        total += i
        count += 1
print(total, count)