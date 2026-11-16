# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findPos(self,root,val,pos):
        if not root:
            return
        pos[0] = root
        if root.val < val:
            self.findPos(root.right,val,pos)
        else:
            self.findPos(root.left,val,pos)
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        pos = [None]
        self.findPos(root,val,pos)
        # print(f"This is pos: {pos[0].val}")
        if not pos[0]:
            return TreeNode(val = val)
        elif pos[0].val > val:
            pos[0].left = TreeNode(val = val)
        else:
            pos[0].right = TreeNode(val = val)
        return root
        
            