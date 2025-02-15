class Solution:
    def jump(self, nums: List[int]) -> int:
        near = far = jumps = 0
        while far < len(nums) - 1:
            farthest = 0
            for i in range(near, far + 1):
                farthest = max(farthest, i + nums[i])
            near = far + 1
            far = farthest
            jumps += 1
        return jumps
        """
        gas = 0
        count = 0
        n = len(nums)
        pos = 0

        while pos < n-1:
            gas = nums[pos]
            print(pos)
            if pos + gas >= n-1:
                count += 1
                break
            preview = nums[pos+1:pos+1+gas]
            farthest_cal = -1000
            for i in range(gas):
                if preview[i] - (gas - i + 1) > farthest_cal:
                    farthest_cal = preview[i] - (gas - i + 1)
                    farthest = i

            pos = pos + farthest + 1
            count += 1
        
        return count
        """
