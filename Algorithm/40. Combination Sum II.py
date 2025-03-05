class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        subsets = []
        candidates.sort()
        def dfs(idx, subset, sum_subset):
            if sum_subset > target:
                return
            if sum_subset == target:
                subsets.append(subset[:])
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                subset.append(candidates[i])
                sum_subset += candidates[i]
                dfs(i + 1, subset, sum_subset)
                subset.pop()
                sum_subset -= candidates[i]

        dfs(0, [], 0)
        return subsets
