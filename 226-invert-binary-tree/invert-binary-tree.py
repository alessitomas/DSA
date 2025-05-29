# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# pre - order invertion

# flip
# explore left
# explore right



# flp the tree
# every direct node children is flipped

# dfs(root) = flip(root) + dfs(left) + dfs(right)

class Solution:
    def iterative_dfs(self, root):
        stack = [root]

        while len(stack) > 0:
            
            node = stack.pop(-1)
            # flip
            node.left, node.right = node.right, node.left
            
            
            if node.left is not None:
                stack.append(node.left)
            
            if node.right is not None:
                stack.append(node.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        self.iterative_dfs(root)
        return root

        

        