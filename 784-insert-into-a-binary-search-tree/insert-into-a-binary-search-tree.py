# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val)
        if (not root):
            root = new_node
            return root

        current = root
        
        while (current):
            if (val < current.val):
                if (not current.left):
                    current.left = new_node
                    break
                current = current.left
            
            else:
                if (not current.right):
                    current.right = new_node
                    break
                current = current.right
        
        return root
        