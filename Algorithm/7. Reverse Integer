class Solution:
    def reverse(self, x: int) -> int:
        # Time = O(1)
        # Space = O(1)
        max_no = 2 ** 31 - 1
        min_no = -2 ** 31
        pos = True
        x = str(x).strip()
        if x[0] == "-":
            pos = False
            x = x[1:]
        result = x[::-1]
        if pos == True:
            result = int(result)
        else:
            result = -int(result)
        if result < min_no or result > max_no:
            return 0
        else:
            return result

    def reverse2(self, x: int) -> int:
        # Time = O(1)
        # Space = O(1)
        max_no = 2 ** 31 - 1
        min_no = -2 ** 31
        is_pos = True
        if x < 0:
            is_pos = False
            x *= -1
        res = 0
        while x > 0:
            res = (res * 10) + (x % 10)
            x = x // 10
        if res < min_no or res > max_no:
            return 0
        return res if is_pos else -res
