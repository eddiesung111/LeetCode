mod = 10 ** 9 + 7
@cache
def dp_recursive(i,j,k):
    if i == 0:
        return 1
    ans = dp_recursive(i-1, j, 0)
    if j < 1:
        ans += dp_recursive(i-1, 1, 0)
    if k < 2:
        ans += dp_recursive(i-1, j, k + 1)
    return ans % mod

class Solution:
    def checkRecord(self, n: int) -> int:
        # Time = O(n)
        # Space = O(n)
        return dp_recursive(n, 0, 0)

    def checkRecord2(self, n: int) -> int:
        # Time = O(n)
        # Space = O(n)
        mod = 1000000007
        dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n + 1)]
        dp[0][0][0] = 1
        for i in range(1, n + 1):
            for count_a in range(2):
                for count_l in range(3):
                    # Insert P
                    dp[i][count_a][0] = (dp[i][count_a][0] + dp[i - 1][count_a][count_l]) % mod
                    
                    # Insert A
                    if count_a > 0:
                        dp[i][count_a][0] = (dp[i][count_a][0] + dp[i - 1][count_a - 1][count_l]) % mod
                    # Insert L
                    if count_l < 2:
                        dp[i][count_a][count_l + 1] = (dp[i][count_a][count_l + 1] + dp[i - 1][count_a][count_l]) % mod
        return sum(dp[n][count_a][count_l] for count_a in range(2) for count_l in range(3)) % mod
