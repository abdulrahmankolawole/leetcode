# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        is_sym = True
        def traverse(node1, node2):
            nonlocal is_sym
            if (not node1 and not node2):
                return
            if (not node1 or not node2 or node1.val != node2.val):
                is_sym = False
                return True
            
            traverse(node1.left, node2.right)
            traverse(node1.right, node2.left)
            return is_sym
        
        return traverse(root, root)
        