# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def summation(root, s):
            if not root:
                return 0
            
            s = s * 10 + root.val
            if not root.left and not root.right:
                return s

            return summation(root.left, s) + summation(root.right, s)

        return summation(root, 0)

