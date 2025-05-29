# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# pre order traversal
# sameTree(a,b) = a.val == b.val and sameTree(a.left,b.left) and sameTree(a.right,b.right)

# base case

# none and none -> T
# x and none -> F
# none and y -> F

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # none and none -> T
        if p is None and q is None:
            return True
        # x and none -> F
        # none and y -> F
        if p is None or q is None:
            return False
        # diff 
        if p.val != q.val:
            return False
        
        # left sub
        left_sub = self.isSameTree(p.left, q.left)
        if not left_sub:
            return False
        
        # right sub
        right_sub = self.isSameTree(p.right, q.right)
        if not right_sub:
            return False

        return True
        