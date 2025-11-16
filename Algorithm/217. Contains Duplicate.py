class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Time = O(n)
        # Space = O(n)
        seen = set()
        for num in nums:
            if num in seen:
                return True
            if num not in seen:
                seen.add(num)
        return False
