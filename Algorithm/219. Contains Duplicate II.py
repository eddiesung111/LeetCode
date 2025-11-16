class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Time = O(n)
        # Space = O(n)
        seen = set()
        length = 0
        n = len(nums)
        for i in range(len(nums)):
            if length > k:
                seen.remove(nums[i - 1 - k])
                length -= 1
            if nums[i] in seen:
                return True
            else:
                seen.add(nums[i])
                length += 1
        return False
