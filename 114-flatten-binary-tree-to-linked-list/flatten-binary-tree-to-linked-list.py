# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        preorder = []

        if (not root):
            return root

        def dfs(node):
            if (not node):
                return None
            
            preorder.append(node)
            if (node.left):
                dfs(node.left)
            if (node.right):
                dfs(node.right)

        dfs(root)
        
        print(preorder)
        for i in range(len(preorder) - 1):
            preorder[i].left = None
            preorder[i].right = preorder[i + 1]

        return preorder[0]
        