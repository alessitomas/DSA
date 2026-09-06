# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""

naive dfs that will expore all nodes

time: O(N)
space: O(N)


given that the input is a BST




if p and q are in different subtrees root is the LCA
if p or q is the root than root is LCA

else explore only the subtree that contains p and q 


to be in the left subtree


node.val <= root.val

to be in the right subtree 

node.val > root.val


"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None

        def find_lca(root, p, q):
            if root == p or root == q:
                return root
            
            p_is_left = p.val <= root.val
            q_is_left = q.val <= root.val 

            if p_is_left != q_is_left:
                return root
            
            subtree = root.left
            
            if not p_is_left:
                subtree = root.right
            
            return find_lca(subtree,p,q)

            

        
        
        return find_lca(root, p, q)




        
