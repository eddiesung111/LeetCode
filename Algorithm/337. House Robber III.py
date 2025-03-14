# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
    # Time = O(N)
    # Space = O(N)
        def dfs(root):
            if not root:
                return (0, 0)
            our_left = dfs(root.left)
            our_right = dfs(root.right)
            return (max(our_left) + max(our_right), root.val + our_left[0] + our_right[0])
        return max(dfs(root))

    @cache
    def rob2(self, root: Optional[TreeNode]) -> int:
        # Time = O(N)
        # Space = O(N)
        if not root:
            return 0
        dont_rob, rob_root = self.rob(root.left) + self.rob(root.right), root.val
        if root.left:
            rob_root += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            rob_root += self.rob(root.right.left) + self.rob(root.right.right)
        return max(dont_rob, rob_root)
