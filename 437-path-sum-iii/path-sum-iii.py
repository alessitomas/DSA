# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root, cumulative_path, targetSum):
            if root is None: return 0
            cur_paths = 0
            for i in range(0, len(cumulative_path)):
                val = cumulative_path[i]
                if val + root.val == targetSum:
                    cur_paths += 1
                cumulative_path[i] += root.val
            if root.val == targetSum:
                cur_paths += 1

            cumulative_path.append(root.val)

            pos_left = dfs(root.left, cumulative_path, targetSum)
            pos_right = dfs(root.right, cumulative_path, targetSum)

            cumulative_path.pop(-1)

            for i in range(0, len(cumulative_path)):
                cumulative_path[i] -= root.val
 

            return pos_left + pos_right + cur_paths
        return dfs(root, [], targetSum)
            



        