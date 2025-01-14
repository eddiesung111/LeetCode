class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        result = ""
        for i in range(n):
            j = (i+k) % n
            result += s[j]
        return result
