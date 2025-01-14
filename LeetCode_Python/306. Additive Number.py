class Solution:
    # Time: O(n^3)
    # Space: O(n)
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def is_valid(first, second, remaining):
            while remaining:
                third = first + second
                third_str = str(third)
                if not remaining.startswith(third_str):
                    return False
                first, second = second, third
                remaining = remaining[len(third_str):]
            return True

        for i in range(1, n):
            for j in range(i + 1, n):
                first = num[:i]
                second = num[i:j]

                if (len(first) > 1 and first[0] == "0") or (
                    len(second) > 1 and second[0] == "0"
                ):
                    continue
                first = int(first)
                second = int(second)
                remaining = num[j:]
                if is_valid(first, second, remaining):
                    return True
        return False

