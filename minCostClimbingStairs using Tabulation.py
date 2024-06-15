def minCostClimbingStairs(cost):
    n = len(cost)
    if n == 0:
       return 0
    if n == 1:
       return cost[0]

    dp = [0] * n
    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

    return min(dp[n - 1], dp[n - 2])

n = int(input("Enter the number of stairs: "))
cost = []
for i in range(n):
    cost.append(int(input(f"Enter the cost of stair {i + 1}: ")))

print(minCostClimbingStairs(cost))