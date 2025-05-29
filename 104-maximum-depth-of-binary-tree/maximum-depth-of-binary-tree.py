# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# depth
# number of nodes along the longest path

# depth(root) = 1  + max(depth(root.left), depth(root.right))
# if root is None: 0


class Solution:
    def dfs_max_path(self, root):
        if root is None:
            return 0
        return \
            1 + max(self.dfs_max_path(root.left), self.dfs_max_path(root.right))
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.dfs_max_path(root)
        