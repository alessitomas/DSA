# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# dfs
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # lca, has_p_or_q
        def dfs_rec(root, p, q):
            
            if root is None:
                return None, False

            
            lca_left, has_node_left = dfs_rec(root.left, p, q)
            
            if lca_left:
                return lca_left, True

            lca_right, has_node_right = dfs_rec(root.right, p, q)

            if lca_right:
                return lca_right, True 


            if has_node_left and has_node_right:
                return root, True
            
            is_root = (root == p or root == q)
            
            if (has_node_left or has_node_right) and is_root:
                return root, True

            return None, is_root or has_node_left or has_node_right
        

        lca, _ = dfs_rec(root, p, q)
        return lca
