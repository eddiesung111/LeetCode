class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        result = 0
        max_heap = []

        for i in range(m):
            grid[i] = [-i for i in grid[i]]
            heapq.heapify(grid[i])
        
        for col in range(n):
            temp = 0
            for row in range(m):
                if grid[row][0] < temp:
                    temp = grid[row][0]
                heapq.heappop(grid[row])
            result += temp

        return -result
