class Solution:
    """
    def canJump(self, nums: List[int]) -> bool:
        gas = 0
        for num in nums:
            if gas < 0:
                return False
            
            elif num > gas:
                gas = num
            gas -= 1
        return True
        """
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        final = n - 1
        for idx in reversed(range(n - 1)):
            if idx + nums[idx] >= final:
                final = idx
        
        return final == 0
