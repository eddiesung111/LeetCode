class Solution:
    def minTimeToType(self, word: str) -> int:
        n = len(word)
        curr = 'a'
        result = 0
        for idx in range(n):
            result += min(abs(ord(word[idx]) - ord(curr)), 26 - abs(ord(word[idx]) - ord(curr)))
            result += 1
            curr = word[idx]
        return result

