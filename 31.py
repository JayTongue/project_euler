def count(target, coins):
    ways = [0] * (target + 1) # so list with 201 0's
    ways[0] = 1 # one way to make zero p
    for coin in coins:
        for amount in range(coin, target + 1):
            ways[amount] += ways[amount - coin] #still compute all possibilities, but add a count of each result
    return ways[target]
print(count(200, [1, 2, 5, 10, 20, 50, 100, 200]))