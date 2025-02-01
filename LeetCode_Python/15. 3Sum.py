class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Time = O(n^2)
        # Space = O(n), since Python sorting take O(n) space
        n = len(nums)
        result = []
        nums.sort()
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum > 0:
                    right -= 1
                elif curr_sum < 0:
                    left += 1
                else:
                    result.append([nums[i] ,nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        nums.sort()
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n-1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                for k in range(j+1,n):
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.append([nums[i],nums[j],nums[k]])
        return result
