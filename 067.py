with open('data/67.txt', 'r') as data:
    data = data.readlines()
    data = [list(map(int, line.split(' '))) for line in data]

new_bottom = [i + (max(data[-1][count], data[-1][count+1])) for count, i in enumerate(data[-2])]
for line_counter in range(3, len(data)+1):
    new_bottom = [i + max(new_bottom[count], new_bottom[count+1]) for count, i in enumerate(data[-line_counter])]
print(new_bottom[0])
