# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        result = 0
        def traverse(node, maxVal):
            if not node:
                return
            nonlocal result

            if (node.val >= maxVal):
                result += 1
            maxVal = max(maxVal, node.val)

            traverse(node.left, maxVal)
            traverse(node.right, maxVal)

        traverse(root, root.val)
        
        return result
        