# 102. Binary Tree Level Order Traversal
# dfs
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        res = []
        self.order(root, 0, res)
        return res
    
    def order(self, root, index, res):
        if root:
            if len(res) < index+1:
                res.append([])
            res[index].append(root.val)
            self.order(root.left, index+1, res)
            self.order(root.right, index+1, res)