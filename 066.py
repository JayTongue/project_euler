import math

def solve_pell(d):
    m, d_, a = 0, 1, int(math.isqrt(d))
    if a * a == d:
        return None  # perfect square, skip

    num1, num = 1, a
    den1, den = 0, 1
    a0 = a

    while num * num - d * den * den != 1:
        m = d_ * a - m
        d_ = (d - m * m) // d_
        a = (a0 + m) // d_
        num1, num = num, a * num + num1
        den1, den = den, a * den + den1

    return num  # minimal x

def main():
    max_x = 0
    result_d = 0

    for D in range(2, 1001):
        x = solve_pell(D)
        if x and x > max_x:
            max_x = x
            result_d = D

    print(result_d)

if __name__ == "__main__":
    main()
