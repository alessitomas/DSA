# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Time: O(N)
# Space: O(N)
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        target_sum_updated = targetSum - root.val
        if root.left is None and root.right is None:
            return target_sum_updated == 0
        return self.hasPathSum(root.left, target_sum_updated) or self.hasPathSum(root.right, target_sum_updated)
                 
            
        