# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



# f(node) = abs(f(node.left) - f(node.right)) <= 1, max(f(node.left) , f(node.right)) + 1

# information needed per node: height matched and cur_height

# base case: None height 0
# use -1 for a not balenced case

class Solution:
    def dfs_compare_height(self, root):
        if root is None:
            return 0
        
        l_height = self.dfs_compare_height(root.left)
        r_height = self.dfs_compare_height(root.right)

        if l_height == -1 or r_height == -1:
            return -1

        if abs(r_height - l_height) > 1:
            return -1
        
        return max(l_height, r_height) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return self.dfs_compare_height(root) > 0

        