# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        has_path = False

        def traverse(node, currentSum):
            nonlocal has_path
            if (not node or has_path):
                return 

            currentSum += node.val
            if (not node.left and not node.right and currentSum == targetSum):
                has_path = True
                return 

            traverse(node.left, currentSum )
            traverse(node.right, currentSum)
        traverse(root, 0)
        return has_path
        