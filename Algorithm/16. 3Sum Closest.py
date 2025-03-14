class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Time = O(n^2)
        # Space = O(1)
        nums.sort()
        cloest_sum = float('inf')
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if abs(curr_sum - target) < abs(cloest_sum - target):
                    cloest_sum = curr_sum
                if curr_sum == target:
                    return curr_sum
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1
        return cloest_sum
