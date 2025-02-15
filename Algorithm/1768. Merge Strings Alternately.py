class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Time = O(n+m)
        # Space = O(n+m)
        res = ''
        long = (len(word1) >= len(word2))
        for i in range(min(len(word1), len(word2))):
            res += word1[i]
            res += word2[i]
        if long == True:
            for idx in range(i+1, len(word1)):
                res += word1[idx]
        else:
            for idx in range(i+1, len(word2)):
                res += word2[idx]
        return res
