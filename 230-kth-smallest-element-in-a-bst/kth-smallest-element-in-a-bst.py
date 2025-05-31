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
 

# worst case O(N), when k == N
# O( (K / Height) rounded up )

# the op needs to be done in less than (N) 

# insetion -> N + 1
# deletion -> N - 1

# kth - > 3
# idx_node_map = {0 : node(1), 1: node(2) ...}
# order = 1 - 2 - 4 - 5
# idx_node_map

# insertion(3)
# order = 1 - 2 - 3 - 4 - 5
# order[kth -1]


# create minHeap from the tree
# kth smallest k * log N


# insertion Log N

# removal kt * Log N

class Solution:
    # 5, 3
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return None
        
        # kth, k
        def in_order_traversal_iterative(root, k):
            stack = []
            cur_node = root
            
            while cur_node is not None or len(stack) > 0:
                while cur_node is not None:
                    stack.append(cur_node)
                    cur_node = cur_node.left

                # visit
                cur_node = stack.pop()
                k -= 1
                if k == 0:
                    return cur_node.val
                
                cur_node = cur_node.right
        return in_order_traversal_iterative(root, k)








        kth = in_order_traversal(root, k)
        return kth