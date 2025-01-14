class Solution:
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = nums[0:k]
        heapq.heapify(min_heap)
        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, num)
        return min_heap[0]
    """
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(left, right):
            pivot = nums[right]
            j = left
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1
            
            nums[j], nums[right] = nums[right], nums[j]

            if k < j:
                return quickSelect(left, j-1)
            elif k > j:
                return quickSelect(j+1, right)
            else:
                return nums[k]
        return quickSelect(0, len(nums) - 1)
