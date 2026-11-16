# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def remove(self,root,parent,target):
        if not root:
            return
        self.remove(root.left,root,target)
        self.remove(root.right,root,target)
        if not root.left and not root.right and root.val == target:
            # leaf node
            
            if parent and parent.left == root:
                parent.left = None
            
            elif parent and parent.right == root:
                parent.right = None
            root.val = None
            del root
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        self.remove(root,None,target)
        if not root.val:
            return None
        return root
