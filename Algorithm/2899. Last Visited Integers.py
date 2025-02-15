class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen = []
        ans = []
        count = 0
        for idx in range(len(nums)):
            if nums[idx] > -1:
                seen.insert(0, nums[idx])
                count = 0
            else:
                count += 1
                if count <= len(seen):
                    ans.append(seen[count - 1])
                else:
                    ans.append(-1)
        return ans
            
