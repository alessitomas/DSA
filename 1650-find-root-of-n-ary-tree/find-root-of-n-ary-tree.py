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


visit all children nodes once, mark the only node that was no visited it must be the root! 

N-ary tree has only reference to children and not to the parent 


visiting all nodes once

loop through tree O(N):

dfs() if visited just return, if not explore

total work here:

if already visited O(1), 

total work is O(N) + n * O(1) (from every parent trying to visit it again, or from the nood already visited on the list)

time: O(N)
space: O(N), keep track of visited in a set 



"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        visited = set()

        # visiting successors
        def dfs(node, root):
            if not node or node in visited:
                return
            
            if root != node: # don't visit root
                visited.add(node)

            for c in node.children:
                dfs(c, root)

        for node in tree:
            dfs(node, node)

        for node in tree:
            if node not in visited:
                return node

    


        