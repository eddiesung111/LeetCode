class Solution:
    def myAtoi(self, s: str) -> int:
        # Time = O(n)
        # Space = O(1)
        result = 0
        s = s.strip(" ")
        if len(s) == 0:
            return 0
        neg = False
        if s[0] == '+':
            s = s[1:]
        elif s[0] == '-':
            neg = True
            s = s[1:]
        s = s.lstrip("0")
        for i in range(len(s)):
            if s[i].isdigit():
                result = 10 * result + int(s[i])
            else:
                break
        if neg:
            result = - result
        if result < -2 ** 31:
            result = -2 ** 31
        if result > 2 ** 31 - 1:
            result = 2 ** 31 - 1
        return result
