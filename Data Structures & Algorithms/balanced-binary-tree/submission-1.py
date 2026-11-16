# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self,root,ans):
        if not root:
            return 0
        left = self.height(root.left,ans)
        right = self.height(root.right,ans)
        if abs(left-right) > 1:
            ans[0] = False
        return 1 + max(left,right)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
       ans = [True]
       self.height(root,ans)
       return ans[0]