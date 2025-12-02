class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Time = O(n)
        # Space = O(1)
        prefix, suffix= 1, 1
        n = len(nums)
        res = [1] * n
        for i in range(1, n):
            prefix *= nums[i-1]
            res[i] *= prefix
        for i in range(n-2, -1, -1):
            suffix *= nums[i+1]
            res[i] *= suffix
        return res

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        # Time = O(n)
        # Space = O(1)
        mul = 1
        zero_pos = -1
        for i in range(len(nums)):
            if nums[i] == 0 and zero_pos == -1:
                zero_pos = i
                continue
            mul *= nums[i]
        if mul == 0:
            return [0] * len(nums)
        else:
            if zero_pos == -1:
                for i in range(len(nums)):
                    nums[i] = int(mul / nums[i])
                return nums
            else:
                temp = [0] * len(nums)
                temp[zero_pos] = mul
                return temp
