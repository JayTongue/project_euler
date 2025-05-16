total_days, start = 0, 2
non_leap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def align_sundays(months_list, start):
    sunday_count = 0
    for month in months_list:
        if start == 0:
            sunday_count += 1
        start = (start + month) % 7
    return sunday_count, start

for year in range(1901, 2001):
    if not year % 4:
        sunday_count, start = align_sundays(leap, start)
    else :
        sunday_count, start = align_sundays(non_leap, start)
    total_days += sunday_count
print(total_days)

