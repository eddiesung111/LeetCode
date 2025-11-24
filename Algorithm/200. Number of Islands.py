class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Time = O(mn)
        # Space = O(mn)
        m, n = len(grid), len(grid[0])
        island = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def bfs(i, j):
            queue = deque()
            grid[i][j] = '0'
            queue.append((i, j))
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc <n and grid[nr][nc] == '1':
                        queue.append((nr,nc))
                        grid[nr][nc] = "0"
            return
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    island += 1
                    bfs(i, j)
        return island
                    
