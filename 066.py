# # from math import isqrt
# from tqdm import tqdm
# from numba import jit, njit

# @njit
# def isqrt(n):
#     if n == 0 or n == 1:
#         return n
#     x = n
#     y = (x + 1) // 2
#     while y < x:
#         x = y
#         y = (x + n // x) // 2
#     return x


# @njit
# def diophantine(d):
#     x = 2
#     while True:
#         numerator = x**2 - 1
#         if numerator % d == 0:
#             y_cut = numerator//d
#             y = isqrt(y_cut)
#             if y * y == y_cut:
#                 return x
        
#         x += 1


# search_space = 100
# non_squares = [True for _ in range(search_space)]
# i = 1
# while True:
#     if i**2 < search_space:
#         non_squares[i**2] = False
#     else:
#         break
#     i += 1

# #find minimal solution given a value of D
# largest_pair = (0, 0)
# for count, bool_val in tqdm(list(enumerate(non_squares))):
#     if bool_val and count > 2:
#         x = diophantine(count)
#         if x > largest_pair[0]:
#             largest_pair = (x, count)
#             # print(largest_pair)
# print(largest_pair)
        
from numba import njit
from tqdm import tqdm


@njit
def isqrt(n):
    if n == 0 or n == 1:
        return n
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


@njit
def diophantine(d):
    x = 2
    while True:
        numerator = x * x - 1
        if numerator % d == 0:
            y_cut = numerator // d
            y = isqrt(y_cut)
            if y * y == y_cut:
                return x
        x += 1


def main():
    search_space = 100
    # Mark non-squares up to search_space
    non_squares = [True] * search_space
    for i in range(1, isqrt(search_space) + 1):
        if i * i < search_space:
            non_squares[i * i] = False

    largest_pair = (0, 0)
    for d, is_non_square in tqdm(list(enumerate(non_squares))):
        if is_non_square and d > 2:
            x = diophantine(d)
            if x > largest_pair[0]:
                largest_pair = (x, d)

    print(largest_pair)


if __name__ == "__main__":
    main()
