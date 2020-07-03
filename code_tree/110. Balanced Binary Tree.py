# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        if abs(self.Height(root.left)-self.Height(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
    
    def Height(self, root):
        if root == None:
            return 0
        return max(self.Height(root.left), self.Height(root.right))+1
        
        