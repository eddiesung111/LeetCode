class Solution:
    # Time = O(n)
    # Space = O(1)
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        n = len(nums)
        count = 0
        prod = 1
        left = 0
        for right in range(n):
            prod *= nums[right]
            while prod >= k and left <= right:
                prod /= nums[left]
                left += 1
            count += right - left + 1
        return count
