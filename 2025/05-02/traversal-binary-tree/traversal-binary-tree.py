# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.lister = []
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if root == None:
            return self.lister

        self.lister.append(root.val)

        if root.left != None:
            self.preorderTraversal(root.left)

        if root.right != None:
            self.preorderTraversal(root.right)

        return self.lister
    
        