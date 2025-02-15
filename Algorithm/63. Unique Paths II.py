class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[1 for _ in range(n)] for _ in range(m)]

        for idx_i in range(m):
            if obstacleGrid[idx_i][0] == 1:
                for row in range(idx_i, m):
                    dp[row][0] = 0
                break

        for idx_j in range(n):
            if obstacleGrid[0][idx_j] == 1:
                for col in range(idx_j,n):
                    dp[0][col] = 0
                break

        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
