# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self,root):
        if not root:
            return [True,0]
        isBL,leftH = self.height(root.left)
        isBR, rightH = self.height(root.right)

        if not isBL or not isBR or abs(leftH-rightH)> 1:
            return [False,float('inf')]
        return [True,max(leftH,rightH)+1]

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root)[0]