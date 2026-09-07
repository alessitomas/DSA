# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""

1. data that I want to pass down is the targets 
2. data that I want to pass up is if at least one of the targets is in the subtree rooted at node
3. postordem traversal. Using the return of the left and right subtree to define the global LCA


"""

# look out for none node deference
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = None

        def dfs_lca(node, p, q):
            nonlocal lca

            if node is None:
                return False

            left = dfs_lca(node.left, p, q)
            right = dfs_lca(node.right, p, q)
            is_root = (node is p) or (node is q)

            if (left and right) or ((left or right) and is_root):
                lca = node
                return True

            return left or right or is_root

        dfs_lca(root, p, q)
        
        return lca 


        