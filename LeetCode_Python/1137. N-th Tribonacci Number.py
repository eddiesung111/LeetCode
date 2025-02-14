class Solution:
    def tribonacci(self, n: int) -> int:
        # Time = O(n)
        # Space = O(1)
        a, b, c, d = 0, 1, 1, 2
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        d = 2
        for _ in range(4,n+1):
            temp = d + d - a
            a, b, c = b, c, d
            d = temp
        return d
