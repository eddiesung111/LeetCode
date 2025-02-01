class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        # Time = O(nk)
        # Space = O(nk)
        n = len(nums)
        def dfs(pos, k):
            if pos == n:
                return 0
            if k < 0:
                return float('inf')
            if dp[k][pos] != -1:
                return dp[k][pos]
            max_num = 0
            total_sum = 0
            min_waste = float('inf')

            for i in range(pos, n):
                max_num = max(max_num, nums[i])
                total_sum += nums[i]
                wasted = max_num * (i - pos + 1) - total_sum
                min_waste = min(min_waste, wasted + dfs(i + 1, k - 1))
            dp[k][pos] = min_waste
            return dp[k][pos]
        dp = [[-1 for _ in range(n)] for _ in range(k+1)]
        return dfs(0, k)
    
    def minSpaceWastedKResizing2(self, nums: List[int], k: int) -> int:
        # Time = O(n^2 * k)
        # Space = O(nk)
        n = len(nums)
        @lru_cache(None)
        def dfs(pos, k):
            if pos == n:
                return 0
            if k < 0:
                return float('inf')
            max_num = 0
            total_sum = 0
            min_waste = float('inf')

            for i in range(pos, n):
                max_num = max(max_num, nums[i])
                total_sum += nums[i]
                wasted = max_num * (i - pos + 1) - total_sum
                min_waste = min(min_waste, wasted + dfs(i + 1, k - 1))
            return min_waste
        return dfs(0, k)
