# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxValue, count):
            if not node:
                return count
            
            if node.val >= maxValue:
                count += 1
                maxValue = node.val
            count = dfs(node.left, maxValue, count)
            count = dfs(node.right, maxValue, count)
            return count
        return dfs(root, root.val, 0)
            