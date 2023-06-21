# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root, key):
        if root is None:
            return None

        if root.val == key:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                successor = self.findSuccessor(root.right)
                root.val = successor.val
                root.right = self.deleteNode(root.right, successor.val)

        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)

        return root
# smallest value in the right subtree of a node to be delete
    def findSuccessor(self, node):
        while node.left is not None:
            node = node.left
        return node

        