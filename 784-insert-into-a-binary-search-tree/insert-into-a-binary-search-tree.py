# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



# 30
#          7
#     3.        25
#. 0.    6.         None


# node(6).left  <- Node(4)
# node(3).right = node(6)
# node(7).left = node(3)
# reurn node 7
# call stack
# O(log N)
class Solution:
    # node(7), 4
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        # return the cur node
        def dfs_find_postion(root, val):
            if root is None:
                return TreeNode(val)
            # go right
            if val > root.val:
                root.right = dfs_find_postion(root.right, val)
            else: 
                root.left = dfs_find_postion(root.left, val)
            
            return root
        # node(7), 4
        return dfs_find_postion(root, val)