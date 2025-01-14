class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def xor(values: List[int]) -> int:
            result = 0
            for value in values:
                result ^= value
            return result
    
        def generateSubset(nums, pointer, temp, subsets):
            if pointer == len(nums):
                subsets.append(temp[:])
                return
            
            temp.append(nums[pointer])
            generateSubset(nums, pointer + 1, temp, subsets)
            temp.pop()

            generateSubset(nums, pointer + 1, temp, subsets)


        subsets = []
        generateSubset(nums, 0, [], subsets)
        ans = 0
        for subset in subsets:
            ans += xor(subset)
        return ans
