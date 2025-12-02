class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time = O(n)
        # Space = O(1)
        min_seen = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(max_profit, prices[i] - min_seen)
            min_seen = min(min_seen, prices[i])
        return max_profit
