class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for idx in range(len(nums)):
            if nums[idx] != val:
                nums[count] = nums[idx]
                count += 1
        while count < len(nums):
            nums.pop()
            
