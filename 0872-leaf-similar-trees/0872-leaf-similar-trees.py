# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def traverser(root,ans):
            if root is None:
                return ans
            
            if not root.left and not root.right:
                ans.append(root.val)
            traverser(root.right,ans)
            traverser(root.left,ans)
            return ans
        if traverser(root1,[]) == traverser(root2,[]):
            return True 
        return False 

        