class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        # Time = O(3^n)
        # Space = O(k * 2^n)
        n = len(cookies)
        dp = [[float('inf')] * (1 << n) for _ in range(k+1)]
        sum_mask = [0] * (1 << n)
        for mask in range(1 << n):
            total = 0
            for i in range(n):
                if mask & (1 << i):
                    total += cookies[i]
            sum_mask[mask] = total

        dp[0][0] = 0
        for person in range(1, k + 1):
            for mask in range(1 << n):
                submask = mask
                while submask:
                    dp[person][mask] = min(dp[person][mask], max(sum_mask[submask], dp[person - 1][mask ^ submask]))
                    submask = (submask - 1) & mask
        return dp[k][(1 << n) - 1]

    # Time = O(k^n)
    # Space = O(n)
    def distributeCookies2(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        cookies_own = [0] * k
        result = float("inf")
        num_zero = k
        def helper(pos: int, cookies_own: List[int], num_zero: int) -> None:
            nonlocal result
            if num_zero > n - pos:
                return

            if pos == n:
                unfair_ans = max(cookies_own)
                result = min(unfair_ans, result)
                return

            for person in range(k):
                prev_zero = (cookies_own[person] == 0)
                cookies_own[person] += cookies[pos]
                helper(pos + 1, cookies_own, num_zero - prev_zero)
                cookies_own[person] -= cookies[pos]

        helper(0, cookies_own, num_zero)
        return result
