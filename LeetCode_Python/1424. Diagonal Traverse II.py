class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        df = []

        m = len(nums)
        for i in range(m):
            n = len(nums[i])
            for j in range(n):
                df.append((i+j, -i, j))
        
        heapq.heapify(df)
        result = []
        while df:
            result.append(nums[-df[0][1]][df[0][2]])
            heapq.heappop(df)
        
        return result
