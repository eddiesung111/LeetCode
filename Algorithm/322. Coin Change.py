class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Time = O(mn), m = size of coins, n = amount
        # Space = O(n), n = amount
        n = len(coins)
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
        for i in range(amount+1):
            for coin in coins:
                if i - coin >= 0 and dp[i - coin] < float('inf'):
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1] if dp[-1] < float('inf') else -1
