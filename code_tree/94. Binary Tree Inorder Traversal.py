# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        answer = []
        self.inorder(root,answer)
        return answer
        
    def inorder(self,root,answer):
        if root == None:
            return None
        if root.left != None:
            self.inorder(root.left, answer)
        answer.append(root.val)
        if root.right != None:
            self.inorder(root.right, answer)

    

