def pathfinder(width, height):
    start_list = list(range(1, width+2))
    print(start_list)
    for _ in range(height-1):
        next_layer = [0]
        for i in start_list:
            next_layer.append(i + next_layer[-1])
        start_list = next_layer[1:]
        print(start_list)
    return start_list[-1]
    
print(pathfinder(20, 20))