# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return []

        pre_ord = []
        # node
        # left
        # right

        def pre_order_traversal(root):
            if not root:
                return
            
            pre_ord.append(root)
            pre_order_traversal(root.left)
            pre_order_traversal(root.right)

        pre_order_traversal(root)
        
        for i in range(len(pre_ord) - 1):
            cur = pre_ord[i]
            cur.left = None
            cur.right = pre_ord[i+1]
        
        return root