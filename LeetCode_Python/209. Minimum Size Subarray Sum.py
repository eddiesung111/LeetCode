class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        result = float('inf')
        left = 0
        check = 0
        for right in range(n):
            check += nums[right]
            if check >= target:
                while check >= target:
                    check -= nums[left]
                    left += 1
                result = min(result, right - left + 2)

        return result if result < float('inf') else 0            
             
