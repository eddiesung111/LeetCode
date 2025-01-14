class Solution:
    def hammingWeight(self, n: int) -> int:
        return [int(bit) for bit in bin(n)[2:]].count(1)
    """
    def hammingWeight(self, n: int) -> int:
        count = 1
        while n > 1:
            if n % 2 == 1:
                count += 1
            n = n // 2
        return count
    """
