# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return [0,0]
            lwithRoot, lwithoutRoot = dfs(root.left)
            rwithRoot, rwithoutRoot = dfs(root.right)
            return [root.val + lwithoutRoot + rwithoutRoot, max(lwithRoot,lwithoutRoot)+ max(rwithRoot,rwithoutRoot)]
        return max(dfs(root))