class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Time = O(n)
        # Space = O(n)
        count = 0
        curr_sum = 0
        pre_count = {0:1}
        for num in nums:
            curr_sum += num
            complement = curr_sum - k
            if complement in pre_count:
                count += pre_count[complement]
            
            if curr_sum in pre_count:
                pre_count[curr_sum] += 1
            else:
                pre_count[curr_sum] = 1
