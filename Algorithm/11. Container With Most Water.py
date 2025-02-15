class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        n = len(height)
        left = 0
        right = n - 1
        while left < right:
            low = min(height[left], height[right])
            area = (right - left) * low
            result = max(area, result)

            if low == height[left]:
                left += 1
            else:
                right -= 1

        return result
