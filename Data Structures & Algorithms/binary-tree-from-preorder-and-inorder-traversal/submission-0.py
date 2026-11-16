# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findRoot(self,arr, num):
        idx = 0
        while idx < len(arr):
            if num == arr[idx]:
                return idx
            idx += 1
 
      
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) <=0:
            return
        if len(preorder) == 1:
            return TreeNode(val = preorder[0])

        root = TreeNode(preorder[0])
        rootIdx = self.findRoot(inorder, root.val)
      
        root.left = self.buildTree(preorder[1:rootIdx+1],inorder[:rootIdx])
        root.right = self.buildTree(preorder[rootIdx+1:],inorder[rootIdx+1:])
        return root