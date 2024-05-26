def countWays(n):
    if n <= 1:
        return n

    # Initialize a memoization array to store results of subproblems
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    # Calculate ways to reach each stair from the bottom
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

# Example usage
n = 4
print(f"Number of ways = {countWays(n)}")
