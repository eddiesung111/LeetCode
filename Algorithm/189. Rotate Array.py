class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        for _ in range(k):
            nums.insert(0, nums[n-1])
        for _ in range(k):
            nums.pop()
