class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Time = O(n)
        # Space = O(1)
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                return digits
        return [1] + digits
