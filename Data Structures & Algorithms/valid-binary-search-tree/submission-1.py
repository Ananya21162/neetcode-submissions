# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findIfValid(self,root, maxi, mini):
        if not root:
            return True, float('-inf'), float('inf')
        # left, right = True, True
        # if root.left:
        left,leftmax,leftmin = self.findIfValid(root.left,max(maxi,root.val),min(mini,root.val)) # maximum value on left
        # if root.right:
        right,rightmax,rightmin = self.findIfValid(root.right,max(maxi,root.val),min(mini,root.val)) # minimum value on right
        if not left or not right:
            return False, float('inf'), float('-inf')
        elif root.val <= leftmax or root.val >= rightmin:
            return False, float('inf'), float('-inf')
        else:
            return True, max(rightmax,root.val), min(leftmin,root.val)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
       ans, maximum, minimum = self.findIfValid(root,float('-inf'), float('inf'))
       return ans