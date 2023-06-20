# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        #if q or p is root the LCA is root
        if not root or q == root or p == root:
            return root 
        
        left_lca = self.lowestCommonAncestor(root.left, p, q)
        right_lca = self.lowestCommonAncestor(root.right, p,q)

        #both p and q are on different subtress
        if left_lca and right_lca:
            return root
        if left_lca:
            return left_lca
        if right_lca:
            return right_lca
        return None