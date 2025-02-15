class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        sec_max = float("-inf")
        n = len(nums)
        for right in reversed(range(n)):
            if sec_max > nums[right]:
                return True
            while stack and stack[-1] < nums[right]:
                sec_max = stack[-1]
                stack.pop()
            stack.append(nums[right])
        return False
            
