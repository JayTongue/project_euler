from helpers.timer import timer

@timer
def main():
    n = 100
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            dp[j] += dp[j - i]

    print(dp[n] - 1)

main()
