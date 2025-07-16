def spiral(X, Y):
    x = y = 0
    dx, dy = 0, -1
    for _ in range(max(X, Y) ** 2):
        if (-X // 2 <= x < (X + 1) // 2) and (-Y // 2 <= y < (Y + 1) // 2):
            yield x, y
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
            dx, dy = -dy, dx
        x, y = x + dx, y + dy

spiral_matrix_size = 1001
my_list = list(range(spiral_matrix_size ** 2))
my_list = [my_list[i:i + spiral_matrix_size] for i in range(0, len(my_list), spiral_matrix_size)]
diff = spiral_matrix_size // 2

for i, (x, y) in enumerate(spiral(spiral_matrix_size, spiral_matrix_size), start=1):
    my_list[x + diff][y + diff] = i

total = -1 #center will always be 1, start from -1 to negate double-count
for i in range(spiral_matrix_size):
    total += my_list[i][i]
    total += my_list[i][spiral_matrix_size - 1 - i]

print(total)
