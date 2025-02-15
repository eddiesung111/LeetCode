class Solution:
    # Time = O(nlogn + klogn) = O(nlogn)
    # Space = O(n)
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = [(capital[i], profits[i]) for i in range(n)]
        projects.sort()
        idx = 0
        max_capital = []
        while k > 0:
            while idx < n and projects[idx][0] <= w:
                heapq.heappush(max_capital, -projects[idx][1])
                idx += 1
            if not max_capital:
                break
            w -= heapq.heappop(max_capital)
            k -= 1
        return w
