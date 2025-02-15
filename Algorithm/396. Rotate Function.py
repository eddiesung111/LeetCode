class Solution:
    # Time = O(n)
    # Space = O(n)
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        sum_nums = 0
        dp = [0 for _ in range(n)]
        for i in range(n):
            sum_nums += nums[i]
            dp[0] += nums[i] * i
        for i in range(1,n):
            dp[i] = dp[i-1] + sum_nums - n * nums[-i]
        return max(dp)
