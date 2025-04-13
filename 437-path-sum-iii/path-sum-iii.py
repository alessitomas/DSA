# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time O(Nˆ2)
# Space O(N)
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cumulative_paths = {0:1}
        def dfs(root, cumulative_path, targetSum):
            if root is None: return 0
            cumulative_path += root.val
            paths = cumulative_paths.get(cumulative_path - targetSum, 0)

            cumulative_paths[cumulative_path] = cumulative_paths.get(cumulative_path, 0) + 1

            pos_left = dfs(root.left, cumulative_path, targetSum)
            pos_right = dfs(root.right, cumulative_path, targetSum)

            cumulative_paths[cumulative_path] -= 1

            return pos_left + pos_right + paths
        return dfs(root, 0, targetSum)
            



        