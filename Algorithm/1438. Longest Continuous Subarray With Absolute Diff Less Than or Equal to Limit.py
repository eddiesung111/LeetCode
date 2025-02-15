class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        left = 0
        result = 0
        max_deque = deque()  # To store indices of max elements
        min_deque = deque()  # To store indices of min elements

        for right in range(n):
            while max_deque and nums[right] >= nums[max_deque[-1]]:
                max_deque.pop()
            max_deque.append(right)

            while min_deque and nums[right] <= nums[min_deque[-1]]:
                min_deque.pop()
            min_deque.append(right)

            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                if max_deque[0] == left:
                    max_deque.popleft()
                if min_deque[0] == left:
                    min_deque.popleft()
                left += 1
            result = max(result, right - left + 1)
        return result
