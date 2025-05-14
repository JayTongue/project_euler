for i in range(1, 1000):
    for j in range(1, 1000):
        total = (i**2 + j**2) ** (1/2)
        if (i + j + total) == 1000:
            print(i*j*total)
            break