# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        has_path = []

        def traverse(node, currentSum, path):
            nonlocal has_path
            if (not node):
                return 

            currentSum += node.val
            path.append(node.val)
            if (not node.left and not node.right and currentSum == targetSum):
                has_path.append(path) 

            traverse(node.left, currentSum, path[:])
            traverse(node.right, currentSum, path[:])
        traverse(root, 0, [])
        return has_path
        