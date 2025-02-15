class Solution:
    def mincostTickets3(self, days: List[int], costs: List[int]) -> int:
        # Time = O(n)
        # Space = O(n)
        n = len(days)
        last_day = days[-1]
        dp = [0] * (last_day + 1)
        i = 0
        for day in range(1, last_day+1):
            if day < days[i]:
                dp[day] = dp[day - 1]
            else:
                dp[day] = min(dp[max(0, day - 1)] + costs[0], dp[max(0, day - 7)] + costs[1], dp[max(0, day - 30)] + costs[2])
                i += 1
        return dp[last_day]

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # Time = O(n)
        # Space = O(n)
        n = len(days)
        ticket_choice = [1, 7, 30]

        @lru_cache(None)
        def dfs(date_pos):
            if date_pos >= n:
                return 0

            min_cost = float('inf')
            for j in range(3):
                next_pos = date_pos
                while next_pos < n and days[next_pos] < days[date_pos] + ticket_choice[j]:  
                    next_pos += 1
                min_cost = min(min_cost, costs[j] + dfs(next_pos))
            return min_cost
        return dfs(0)
