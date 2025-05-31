# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 1,3 -> None, 2
# 2,3 -> None, 1
# 3,3 -> 3, 3
# 5,3 -> 3, 3
 
class Solution:
    # 5, 3
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # kth, k
        def in_order_traversal(root, k):
            if root is None:
                return (None, k)
            l_sub, k = in_order_traversal(root.left, k)
            if l_sub is not None:
                return (l_sub, k)
            k -= 1  
            # none, 0
            if k == 0:
                return (root.val, k)
            r_sub, k = in_order_traversal(root.right, k)
        
            if r_sub is not None:
                return (r_sub, k)
            return (None, k)
        kth, _ = in_order_traversal(root, k)
        return kth