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

class Solution:
    def dfs_cal_diameter(self, root):
        if root is None:
            return 0, 0
        
        mx_act_l, mx_breaked_l = self.dfs_cal_diameter(root.left)
        mx_act_r, mx_breaked_r = self.dfs_cal_diameter(root.right)
        
        mx_act = max(mx_act_l, mx_act_r) + 1
        cur_breaked = mx_act_l + mx_act_r + 1
        mx_break = max(mx_breaked_l, mx_breaked_r, cur_breaked)

        return mx_act, mx_break
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        _, mx_diameter_nodes = self.dfs_cal_diameter(root)
        return mx_diameter_nodes - 1


        