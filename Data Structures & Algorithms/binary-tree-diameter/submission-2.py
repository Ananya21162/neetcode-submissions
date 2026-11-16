# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findDia(self, root,dia):
        if not root:
            return 0
        left = self.findDia(root.left,dia)
        right = self.findDia(root.right,dia)
        dia[0] = max(dia[0], left+right)
        return 1+ max(left,right)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia = [0]
        self.findDia(root,dia)
        return dia[0]