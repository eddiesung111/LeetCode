class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # Time = O(mn)
        # Space = O(mn)
        m, n = len(matrix), len(matrix[0])
        if m == 0 or n == 0:
            return 0

        max_side = 0
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_side = max(max_side, dp[i][j])
        return max_side * max_side
