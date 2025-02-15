# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time = O(n)
    # Space = O(n)
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:

        def preorder(node: Optional[TreeNode], output, outputs):
            if not node:
                return

            output.appendleft(node.val)
            if not node.left and not node.right:
                outputs.append(list(output)[:])
            else:
                preorder(node.left, output, outputs)
                preorder(node.right, output, outputs)
            output.popleft()
            return
        
        min_num = float('inf')
        outputs = []
        output = deque()
        preorder(root, output, outputs)
        
        min_str = ''.join(chr(val + ord('a')) for val in outputs[0])
        for element in outputs[1:]:
            curr_str = ''.join(chr(val + ord('a')) for val in element)
            min_str = min(min_str, curr_str)
        return min_str
        '''
        min_num = float('inf')
        for element in outputs:
            num = int(''.join(map(str,element)))
            if num < min_num:
                min_num = num
                min_element = element
        return ''.join(chr(val + ord('a')) for val in min_element)
        '''
