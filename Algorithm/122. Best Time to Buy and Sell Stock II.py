class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time = O(n)
        # Space = O(1)
        if len(prices) <= 1:
            return 0
        profit = 0
        for i in range(1, len(prices)):
            net_profit = prices[i] - prices[i-1]
            if net_profit > 0:
                profit += net_profit
        return profit
