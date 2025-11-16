class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Time = O(n)
        # Space = O(1)
        count1, count2 = 0, 0
        major1, major2 = 0, 0
        for num in nums:
            if major1 == num:
                count1 += 1
            elif major2 == num:
                count2 += 1
            elif count1 == 0:
                major1 = num
                count1 += 1
            elif count2 == 0:
                major2 = num
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        count1, count2 = 0, 0
        for num in nums:
            if num == major1:
                count1 += 1
            elif num == major2:
                count2 += 1
        n = len(nums)
        res = []
        if count1 > n // 3:
            res.append(major1)
        if count2 > n // 3:
            res.append(major2)
        return res

    def majorityElement1(self, nums: List[int]) -> List[int]:
        # Time = O(n)
        # Space = O(n)
        n = len(nums)
        count = Counter(nums)
        res = []
        for num in count:
            if count[num] > n // 3:
                res.append(num)
        return res
