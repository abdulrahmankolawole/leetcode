# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        if not root:
            return output
        queue = [root]

        while queue:
            size = len(queue)

            level = []
            for i in range(size):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if (len(output) % 2) == 0:
                output.append(level)
            else :
                output.append(list(reversed(level)))
                # print(level.reverse())

        return output
        
        