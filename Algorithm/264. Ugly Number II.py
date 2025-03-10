class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # Time = O(n)
        # Space = O(n)
        if n == 0:
            return 0
        if n == 1:
            return 1
        t2, t3, t5 = 0, 0, 0
        k = [1 for _ in range(n)]
        for i in range(1,n):
            k[i] = min(k[t2] * 2, k[t3] * 3, k[t5] * 5)
            if k[i] == k[t2] * 2:
                t2 += 1
            if k[i] == k[t3] * 3:
                t3 += 1
            if k[i] == k[t5] * 5:
                t5 += 1
        return k[n-1]
