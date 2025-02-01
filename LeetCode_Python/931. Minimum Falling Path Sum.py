class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # Time = O(mn)
        # Space = O(mn)
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for j in range(n):
            dp[0][j] = matrix[0][j]
        for i in range(1,m):
            for j in range(n):
                dp[i][j] = matrix[i][j] + min(dp[i-1][max(0, j-1)], dp[i-1][j], dp[i-1][min(n-1, j+1)])
        min_val = min(dp[n-1][:])
        return min_val


    def minFallingPathSum2(self, matrix: List[List[int]]) -> int:
        # Time = O(3^n)
        # Space = O(mn)
        m = len(matrix)
        n = len(matrix[0])
        def dfs(idx_i, idx_j):
            if idx_j < 0 or idx_j > n-1:
                return float('inf')
            if idx_i == m:
                return 0
            min_sum = matrix[idx_i][idx_j] + min(dfs(idx_i+1, idx_j), dfs(idx_i+1, idx_j+1), dfs(idx_i+1, idx_j-1))
            return min_sum
        return min(dfs(0, k) for k in range(n))
