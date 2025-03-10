class Solution:
    # Time = O(n)
    # Space = O(n)
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k:
            return '0'
        if k == 0:
            return num
        stack = []
        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        stack = stack[:-k] if k > 0 else stack
        result = ''.join(stack).lstrip('0')
        return result if result else "0"
