class Solution:
    def trap(self, height: List[int]) -> int:
        # Time = O(n)
        # Space = O(1)
        res = 0
        i, j = 0, len(height) - 1
        while i < j and height[i + 1] >= height[i]:
            i = i + 1
        while i < j and height[j - 1] >= height[j]:
            j = j - 1
        max_height = 0
        while i < j:
            curr_height = min(height[i], height[j])
            if max_height < curr_height:
                max_height = curr_height
                if height[i] < height[j]:
                    i = i + 1
                else:
                    j = j - 1
            else:
                if height[i] < height[j]:
                    res += max_height - height[i]
                    i = i + 1
                else:
                    res += max_height - height[j]
                    j = j - 1
        return res
