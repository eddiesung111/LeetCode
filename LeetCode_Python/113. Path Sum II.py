# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Time = O(n)
    # Space = O(n)
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.path = []

        def dfs(root: Optional[TreeNode], curr_sum: int, route: List[int]) -> None:
            if not root:
                return
            
            route.append(root.val)
            curr_sum += root.val

            if not root.left and not root.right:
                if targetSum == curr_sum:
                    self.path.append(route[:])
            else:
                dfs(root.left, curr_sum, route)
                dfs(root.right, curr_sum, route)
            route.pop()
            return
        
        dfs(root, 0, [])

        return self.path
