class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        # Time = O(logn 2^n)
        # Space = O(n)
        n = len(tasks)
        def valid(mid, pos, dist):
            if pos == n:
                return True
            for j in range(mid):
                if tasks[pos] + dist[j] <= sessionTime:
                    dist[j] += tasks[pos]
                    if valid(mid, pos + 1, dist):
                        return True
                    dist[j] -= tasks[pos]
                if dist[j] == 0:
                    break
            return False

        low = 1
        high = n
        while low < high:
            mid = (low + high) >> 1
            dist = [0] * mid
            if valid(mid, 0, dist):
                high = mid
            else:
                low = mid + 1
        return low

    def minSessions2(self, tasks: List[int], sessionTime: int) -> int:
        # Time = O(3^n)
        # Space = O(2^n)
        n = len(tasks)
        sum_mask = [0] * (1 << n)
        for mask in range(1 << n):
            total = 0
            for i in range(n):
                if mask & (1 << i):
                    total += tasks[i]
            sum_mask[mask] = total

        dp = [float('inf')] * (1 << n)
        dp[0] = 0 
        for mask in range(1 << n):
            submask = mask
            while submask:
                if sum_mask[submask] <= sessionTime:
                    other_mask = mask ^ submask
                    dp[mask] = min(dp[mask], dp[other_mask] + 1)
                submask = (submask - 1) & mask
        return dp[-1]
