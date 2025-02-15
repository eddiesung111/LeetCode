class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        for idx in range(1, len(nums)):
            if nums[idx] != nums[idx -1]:
                nums[count] = nums[idx]
                count += 1
        while count < len(nums):
            nums.pop()
