# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNode(self,root,key,parent = None):
        if not root:
            return [None,None]
        
        if root.val == key:
            return [root,parent]
        elif root.val < key:
            parent = root
            return self.findNode(root.right,key,parent)
        else:
            return self.findNode(root.left,key,parent=root)
    
    def findLeftMost(self,node):
        if not node:
            return 
        if not node.left:
            return node
        return self.findLeftMost(node.left)

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        node,parent = self.findNode(root,key)
        # find the leftmost node on right
        if not node:
            return root
        
        if node.left:
            leftmost = self.findLeftMost(node.right)
            if leftmost:
                leftmost.left = node.left
                node.left = None
            else:
                node.right = node.left
        if parent:
            if node == parent.left:
                parent.left = node.right
            else:
                parent.right = node.right

            node.right= None
            del node
            return root
        else:
            return node.right
            