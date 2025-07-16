def find_pal(num):
    num = [int(n) for n in list(str(num))]
    if len(num) == 1:
        return True
    elif len(num) % 2 != 0:
        num.pop(len(num)//2)
    start, end = num[:len(num)//2], num[len(num)-1:len(num)//2-1:-1]
    return start == end

counter = 0
for i in range(int(1e6+1)):
    if find_pal(i) and find_pal(bin(i)[2:]):
        print(i, bin(i)[2:])
        counter += i
print(counter)