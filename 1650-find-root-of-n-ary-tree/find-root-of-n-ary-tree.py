"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

"""

root property

1- Is ancestor of all nodes
2- root does not have a parent

time: O(N)
space: O(N), keep track of visited in a set



"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        total_sum = 0
        visited_sum = 0

        for node in tree:
            if node is None:
                continue
            
            total_sum += node.val
            
            for c in node.children:
                visited_sum += c.val
                
            
        for node in tree:
            if node is None: 
                continue
            
            if node.val == total_sum - visited_sum:
                return node 

    


        