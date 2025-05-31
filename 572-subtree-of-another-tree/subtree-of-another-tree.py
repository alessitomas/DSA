# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#.       3
#     4.   5 

# isSubtree(node3, node4)

# traverse the Tree (root), until we find a node that matches the vale of node of subroot
# than start a dfs that will verify it correctness and structure
# in time complexity when do we consider N+E and when do we consider only N

# O(Nˆ2) , maybe ther is room for improvemnts

class Solution:
    def is_tree_equal(self, tree1, tree2):
        if tree1 is None and tree2 is None:
            return True

        if tree1 is None or tree2 is None:
            return False
        
        if tree1.val != tree2.val:
            return False
        
        return (self.is_tree_equal(tree1.left, tree2.left) and
                self.is_tree_equal(tree1.right, tree2.right))



    # bool 
    # true found a match 
    # false otherwise
    def tree_traversal(self, cur_root, matching_root):
        if cur_root is None:
            return False
        # matching root
        if cur_root.val == matching_root.val:
            # verify if the hole tree matches
            if self.is_tree_equal(cur_root, matching_root):
                return True
        
        return (self.tree_traversal(cur_root.left, matching_root) 
                or self.tree_traversal(cur_root.right, matching_root))
        

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None:
            return False
        
        return self.tree_traversal(root, subRoot)
        

        