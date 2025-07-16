import copy
from helpers.timer import timer

@timer
def main():
    def triangle(n):
        return n*(n+1)//2
    def square(n):
        return n ** 2
    def pentagonal(n):
        return n*(3 * n - 1)//2
    def hexagonal(n):
        return n*(2 * n -1)
    def heptagonal(n):
        return n*(5 * n - 3)//2
    def octagonal(n):
        return n*(3 * n - 2)

    def make_solutions(func):
        func_list = list()
        start = 1
        while True:
            result = func(start)
            if result < int(1e4):
                if result > 1000:
                    func_list.append(result)
                start += 1
            else:
                break
        return func_list

    tria, squa, pent, hexa, hept, octa = map(make_solutions, (triangle, square, pentagonal, hexagonal, heptagonal, octagonal))

    def loop(lists, start, end, solution=[]):
        if len(lists) == 1:
            final = start * 100 + end
            if final in lists[0]:
                solution += [final]
                print(solution, sum(solution))
        for next_list in lists:
            for number in next_list:
                if number // 100 == start:
                    new_lists = copy.deepcopy(lists)
                    new_lists.remove(next_list)
                    loop(new_lists, number % 100, end, solution + [number])

    for num in octa:
        loop([tria, squa, pent, hexa, hept], num % 100, num // 100, [num])

main()