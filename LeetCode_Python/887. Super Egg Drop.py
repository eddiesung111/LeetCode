class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        # Time = O(klogn)
        # Space = O(n)
        dp = [0] * (k + 1)
        m = 0
        while dp[k] < n:
            m += 1
            for i in range(k, 0, -1):
                dp[i] = dp[i - 1] + dp[i] + 1
        return m


    def superEggDrop2(self, k: int, n: int) -> int:
        # Time = O(nk * logn)
        # Space = O(nk)
        if n == 0:
            return 0
        if k == 1:
            return n
        dp = [[0 for _ in range(n+1)] for _ in range(k+1)]
        for i in range(k+1):
            dp[i][1] = 1
        for j in range(n+1):
            dp[1][j] = j
        for i in range(2, k+1):
            for j in range(2, n+1):
                low = 1
                high = j
                temp = 0
                ans = float('inf')
                while low <= high:
                    mid = low + (high - low) // 2
                    left = dp[i-1][mid-1]
                    right = dp[i][j - mid]
                    temp = 1 + max(left, right)
                    if left < right:
                        low = mid + 1
                    else:
                        high = mid - 1
                    ans = min(ans, temp)
                dp[i][j] = ans
        return dp[k][n]
