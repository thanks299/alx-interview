#!/usr/bin/python3
"""
A function that calculates the fewest number of coins needed to make a given amount.
"""
def makeChange(coins, total):
    # Edge case: if total is 0 or less, no coins are needed
    if total <= 0:
        return 0

    # Initialize the dp list with a large number
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make amount 0

    # Update the dp list for each coin
    for amount in range(1, total + 1):
        for coin in coins:
            if amount - coin >= 0:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, it means total cannot be made
    return dp[total] if dp[total] != float('inf') else -1

