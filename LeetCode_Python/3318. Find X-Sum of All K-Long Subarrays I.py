class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        slide = n - k + 1
        result = []

        for num in range(slide):
            result_sum = 0
            temp = nums[num: num + k]
            cache = {}
            for item in temp:
                if item not in cache:
                    cache[item] = 1
                else:
                    cache[item] += 1

            swapped_list = [(-value, -key) for key, value in cache.items()]
            heapq.heapify(swapped_list)

            for count in range(min(x, len(swapped_list))):
                result_sum += swapped_list[0][0] * swapped_list[0][1]
                heapq.heappop(swapped_list)
            result.append(result_sum)

        return result
