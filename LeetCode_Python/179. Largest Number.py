class Solution:
    # Time = O(nlogn)
    # Space = O(n)
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a: str,b: str):
            if a + b > b + a:
                return -1
            return 1
        array = list(map(str, nums))
        sorted_array = sorted(array, key = cmp_to_key(compare))
        if sorted_array[0] == '0':
            return "0"
        return "".join(sorted_array)

    # Time = O(nlogn)
    # Space = O(n)
    def largestNumber2(self, nums: List[int]) -> str:
        def compare(a: int,b: int):
            sa = str(a)
            sb = str(b)
            if sa + sb > sb + sa:
                return -1
            return 1
        nums.sort(key = cmp_to_key(compare))
        if nums[0] == 0:
            return "0"
        return "".join(map(str, nums))
