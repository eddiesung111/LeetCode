class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        result = float("inf")
        n = len(nums)

        for length in range(l, r+1):
            start = 0
            end = start + length
            temp = sum(nums[start:end])
            if temp > 0 and temp < result:
                result = temp
            
            while end <= n-1:
                temp = temp - nums[start] + nums[end]
                if temp > 0 and temp < result:
                    result = temp
                start += 1
                end += 1

        return result if result < inf else -1
