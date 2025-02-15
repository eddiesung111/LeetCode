# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(root, low, high):

            if not root:
                return True
            
            if root.val >= high or root.val <= low:
                return False
            return valid(root.left, low, root.val) and valid(root.right, root.val, high)

        return valid(root, float("-inf"), float("inf"))
