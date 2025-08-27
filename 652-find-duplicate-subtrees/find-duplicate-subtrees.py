# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


""" 


Solution 1:

Brute Force

For every sub tree gets it's signature

Here I can define signature as a tuple of values in a dfs order including None ().

With that I can keep track of which one of the seen seignature and a root for it, and any time that the root was already seen I can add it to a set for the response.


T: O(Nˆ2) where N is the total number of nodes in the tree
S: O(Nˆ2)



Solution 2:

The bottle neck for the first solution was the exploration of paths that were already explored.

Doing a recursive algorihtm is possible to return the signature at each subtree. And compose the signature based on the childrens.

T: O(Nˆ2) where N is the total number of nodes in the tree
S: O(Nˆ2)

signature:
    - left sub, right sub

left, right and mid

post order

{

    (NONE, NONE, 4) : NODE(4),
    (NONE, NONE, 4, NONE, 2): NODE(2),
}

duplicate = {

    NODE(4)
}


                                        1
                                2               3
                            4                 2      4
                                            4               
"""

"""

create_signature(NONE) [None]
create_signature(4) -> [NONE,NONE,4]
create_signature(2)
create_signature(1)
call stack


signature_sub = {
    (NONE,NONE,4) = Node(4)
}


duplicates = {}

"""
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        signature_sub = {}
        duplicates = set() 
        
        if not root:
            return []

        def create_signatures(node):
            if node is None:
                return [None]

            left = create_signatures(node.left) # [NONE,NONE,4]
            right = create_signatures(node.right) # [NONE]

            compose = left + right + [node.val] # [NONE, NONE, 4, NONE]
            signature = tuple(compose) 
            
            if signature in signature_sub:
                duplicates.add(signature_sub[signature])
            else:
                signature_sub[signature] = node
            
            return compose
        
        create_signatures(root)
        return list(duplicates)

            



        