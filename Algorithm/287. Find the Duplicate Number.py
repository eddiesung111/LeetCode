class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Time = O(nlogn)
        # Space = O(1)
        low = 1
        high = len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            count = 0
            for i in range(len(nums)):
                if nums[i] <= mid:
                    count += 1
            if count <= mid:
                low = mid + 1
            else:
                high = mid
        return low
