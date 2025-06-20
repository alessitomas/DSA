class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # Compute the height of the tree
        def get_height(node):
            h = 0
            while node.left:
                h += 1
                node = node.left
            return h
        
        # Check if a node exists at index idx (0-indexed) in the last level
        def is_in_tree(idx, height, node):
            lp, rp = 0, 2**height - 1
            for _ in range(height):
                mid = (lp + rp) // 2
                if idx <= mid:
                    node = node.left
                    rp = mid
                else:
                    node = node.right
                    lp = mid + 1
                if not node:
                    return False
            return True

        height = get_height(root)
        
        if height == 0:
            return 1
        
        # Binary search on last level
        lp, rp = 0, 2**height - 1
        while lp <= rp:
            mid = (lp + rp) // 2
            if is_in_tree(mid, height, root):
                lp = mid + 1
            else:
                rp = mid - 1

        # Total nodes = nodes above last level + nodes in last level
        return (2**height - 1) + lp
