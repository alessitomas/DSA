# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        all_paths = []
        
        if root is None:
            return all_paths

        def list_deep_copy(original_list):
            new_list = []
            for v in original_list:
                new_list.append(v)
            return new_list
        
        def dfs_path_sum(root, targetSum, cur_path, results):
            if root is None:
                return
            
            updated_target = targetSum - root.val
            cur_path.append(root.val)

            if (root.left is None and
            root.right is None and
            updated_target == 0):
                results.append(cur_path)
            
            dfs_path_sum(root.left, updated_target, list_deep_copy(cur_path), results)
            dfs_path_sum(root.right, updated_target, list_deep_copy(cur_path), results)

        dfs_path_sum(root, targetSum, [], all_paths)
        return all_paths
            

            

            


        