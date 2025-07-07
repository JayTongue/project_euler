def check_pal(num):
    num_list = list(str(num))
    if len(num_list) % 2 == 1:
        num_list.pop(len(num_list)//2)
    return num_list[:len(num_list)//2] == num_list[:len(num_list)//2-1:-1]

def reverse_and_add(num):
    reverse_num = int(''.join(list(str(num))[::-1]))
    return num + reverse_num

lychrel = 0
for i in range(1, int(1e4)):
    pal = False
    for j in range(50):
        i = reverse_and_add(i)
        pal = check_pal(i)
        if pal:
            break
    if not pal:
        lychrel += 1
print(lychrel)
