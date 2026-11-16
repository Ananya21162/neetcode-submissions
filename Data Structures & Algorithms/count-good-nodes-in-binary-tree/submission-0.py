# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def Count(self, root, maxV):
        if not root:
            return 0
        if root.val >= maxV[0]:
            return 1 + self.Count(root.left, [root.val]) + self.Count(root.right, [root.val])
        else:
            return self.Count(root.left, maxV) + self.Count(root.right, maxV)

    def goodNodes(self, root: TreeNode) -> int:
        maxV = [float('-inf')]
        return self.Count(root, maxV)
    
        