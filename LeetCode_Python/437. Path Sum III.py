# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time: O(n)
    # Space: O(1)
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        self.targetSum = targetSum
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1
        self.preorder(root, prefix_sums, 0)
        return self.count

    def preorder(self, node, prefix_sums, cumsum):
        if not node:
            return

        cumsum += node.val

        if cumsum - self.targetSum in prefix_sums:
            self.count += prefix_sums[cumsum - self.targetSum]
        prefix_sums[cumsum] += 1

        self.preorder(node.left, prefix_sums, cumsum)
        self.preorder(node.right, prefix_sums, cumsum)
        prefix_sums[cumsum] -= 1


    # Time: O(n^2) if skewed tree, O(nlogn) for balanced tree
    # Space: O(h), h is the height for the tree
    def __init__(self):
        self.count = 0
    
    def pathSum2(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.targetSum = targetSum
        if not root:
            return 0
                
        self.dfs(root, 0)
        self.pathSum(root.left, self.targetSum)
        self.pathSum(root.right, self.targetSum)
        return self.count

    def dfs(self, node: Optional[TreeNode], curr_sum: int) -> None:
        if not node:
            return

        curr_sum += node.val
        if curr_sum == self.targetSum:
            self.count += 1
        
        self.dfs(node.left, curr_sum)
        self.dfs(node.right, curr_sum)
        return
