# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#.       5
#.   4      6    
#. 2           7     


      


# recursive problem
# for every sub tree where I need to remove the root
# I new root will be the first visited node at the right sub tree in order (left, cur, right). because it will be samller value that is higher than the root.
# if the sub tree is empty just use the left sub root, even if it is empty

class Solution:
    def replace_old_root(self, old_root, cur_node):
        cur_prev = old_root
        
        while cur_node.left is not None:
            cur_prev = cur_node
            cur_node = cur_node.left

        cur_prev.left = cur_node.right
        cur_node.left, cur_node.right = old_root.left, old_root.right
        return cur_node

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        def dfs_search_node(root, key):
            if root is None:
                return None
            
            # remove root
            if root.val == key:
                if root.right is None:
                    return root.left
                if root.right.left is None:
                    root.right.left = root.left
                    return root.right
                
                return self.replace_old_root(root, root.right)

            
            if key > root.val:
                root.right = dfs_search_node(root.right, key)
            else:
                root.left = dfs_search_node(root.left, key)

            return root

        return dfs_search_node(root, key)
        
        
        