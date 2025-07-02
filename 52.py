multiple = 6
number = 1
while True:
    numbers = [number * i for i in range(1, multiple+1)]
    if all([sorted(list(str(number))) == sorted(list(str(j))) for j in numbers]):
        print(numbers)
        break
    number += 1