# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# longest path

# base case: Node None return 0

# leaf nodes: return 1

# lg_path(node): 

# max_active_path , max_breaked_path lg_path(node.left)
# max_active_path , max_breaked_path lg_path(node.right)

# node max_active_path = max(mx_left,max_left) + 1
# node mx_brk = (mx_left + max_left + 1, m_b_l, m_b_r)


#        1
#    2.      3 
#  3.   4
#6       5

# Time: O(N)
# Space: O(N)
class Solution:    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        diameter = 0

        def dfs_cal_diameter(root):
            if root is None:
                return 0
            nonlocal diameter 
            
            left_height = dfs_cal_diameter(root.left)
            right_height = dfs_cal_diameter(root.right)

            cur_height = max(left_height, right_height) + 1
            
            diameter = max(diameter, left_height + 1 + right_height)

            return cur_height 

        dfs_cal_diameter(root)
        return diameter - 1


        