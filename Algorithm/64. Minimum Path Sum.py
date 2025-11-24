class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = [[float('inf')] * (n+1) for _ in range(m+1)]
        res[m-1][n] = 0

        for r in reversed(range(m)):
            for c in reversed(range(n)):
                res[r][c] = grid[r][c] + min(res[r+1][c], res[r][c+1])
        return res[0][0]

    def minPathSum1(self, grid: List[List[int]]) -> int:
        # Time = O(mn)
        # Space = O(1)
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0:
                    grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
                elif i > 0:
                    grid[i][j] = grid[i-1][j] + grid[i][j]
                elif j > 0:
                    grid[i][j] = grid[i][j-1] + grid[i][j]
                else:
                    continue
        return grid[m-1][n-1]
