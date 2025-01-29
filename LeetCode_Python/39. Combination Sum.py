class Solution:
    # Time = O(2^n)
    # Space = O(n)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        subsets = []
        subset = []
        length = len(candidates)

        def dfs(pos, path, current_sum):
            if current_sum > target:
                return
            
            if current_sum == target:
                subsets.append(path[:])
                return

            for idx in range(pos, length):
                path.append(candidates[idx])
                dfs(idx, path, current_sum + candidates[idx])
                path.pop()

        dfs(0, subset, 0)
        return subsets
