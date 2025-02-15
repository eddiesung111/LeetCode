class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Time = O(n)
        # Space = O(1)
        j = 0
        for i in range(len(t)):
            if j < len(s) and s[j] == t[i]:
                j += 1
        return (j == len(s))
