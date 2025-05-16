# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        output = []
        if (not root):
            return output

        def traverse(node, currentPath):
            if (not node):
                return
            
            currentPath += str(node.val)
            if (not node.left and not node.right):
                output.append(currentPath)

            if node.left:
                traverse(node.left, currentPath + "->")
            if node.right:
                traverse(node.right, currentPath + "->")
        
        traverse(root, "")
        print(output)
        return output
        