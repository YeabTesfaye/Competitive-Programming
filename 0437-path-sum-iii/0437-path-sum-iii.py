# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # Helper function to perform the depth-first search
        def dfs(node, curr_sum):
            if not node:
                return 0

            count = 0
            if node.val == curr_sum:
                count += 1

            count += dfs(node.left, curr_sum - node.val)
            count += dfs(node.right, curr_sum - node.val)

            return count

        # Main function
        if not root:
            return 0

        total_count = dfs(root, targetSum)
        total_count += self.pathSum(root.left, targetSum)
        total_count += self.pathSum(root.right, targetSum)

        return total_count
