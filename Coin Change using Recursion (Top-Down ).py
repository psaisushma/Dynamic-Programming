def coinChange(coins, amount):
    LARGE_INT = amount + 1
    memo = {}
    def coinChangeRecursive(rem):
        if rem == 0:
            return 0
        if rem < 0:
            return LARGE_INT

        if rem in memo:
            return memo[rem]
        min_coins = LARGE_INT
        for coin in coins:
            result = coinChangeRecursive(rem - coin)
            if result!= LARGE_INT:
                min_coins = min(min_coins, result + 1)
        memo[rem] = min_coins
        return memo[rem]
    result = coinChangeRecursive(amount)
    return result if result!= LARGE_INT else -1
coins = list(map(int, input("Enter the coins (space-separated): ").split()))
amount = int(input("Enter the amount: "))
print(coinChange(coins, amount))