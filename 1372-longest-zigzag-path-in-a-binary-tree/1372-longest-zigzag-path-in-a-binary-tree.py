# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        maxi=0
        def dfs(root,dir,count):
            nonlocal maxi
            if not root:
                return
            if not root.right and not root.left:
                maxi=max(maxi,count)
            if dir and root.left:
                dfs(root.left,False,count+1)
            if not dir and root.left:
                maxi=max(maxi,count)
                dfs(root.left,False,1)
            if not dir and root.right:
                dfs(root.right,True,count+1)
            if dir and root.right:
                maxi=max(maxi,count)
                dfs(root.right,True,1)
    
        if root.right:
            dfs(root.right,True,1)
        if root.left:
            dfs(root.left,False,1)
        
        return maxi