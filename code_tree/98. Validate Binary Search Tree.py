# 98. Validate Binary Search Tree
# BST, recursive
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.Valid(root, float('-inf'), float('inf'))
    
    def Valid(self, root, min, max):
        if not root: 
            return True
        if root.val >= max or root.val <= min:
            return False
        return self.Valid(root.left, min, root.val) and self.Valid(root.right, root.val, max)

