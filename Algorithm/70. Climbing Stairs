class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0 for i in range(n+1)]
        dp[1] = 1
        dp[2] = 2
        for idx in range(3,n+1):
            dp[idx] = dp[idx - 2] + dp[idx - 1]
        return dp[n]
    
    def climbStairs2(self, n: int) -> int:
        def dfs(curr):
            if curr > n:
                return 0
            if curr == n:
                return 1
            return dfs(curr + 1) + dfs(curr + 2)
        return dfs(0)
