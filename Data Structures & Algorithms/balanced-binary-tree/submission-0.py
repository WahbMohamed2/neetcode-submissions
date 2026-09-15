# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if node is None:
                return True,-1

            left_balanced,left_height = check(node.left)
            if not left_balanced:
                return False,0

            right_balanced,right_height = check(node.right)
            if not right_balanced:
                return False,0 

            if abs(left_height - right_height)>1:
                return False,0

            current_height = 1 + max(left_height,right_height)
            return True, current_height
        
        return check(root)[0]
            